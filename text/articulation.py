#!/usr/bin/env python3

import unicodedata
import numpy

class Articulation:
    # Credit to https://martin-thoma.com/word-error-rate-calculation/ (only modification: uint8 => uint32)
    # tl;dr: We calculate a "Levenshtein distance" (# of substitutions, additions, deletions) required
    # We do this "by word" instead of "by letter"

    @staticmethod
    def wer(r, h):
        """
        Calculation of WER with Levenshtein distance.

        Works for input lists whose len fit within 32 bits.
        O(nm) time and space complexity.

        Parameters
        ----------
        r : list
        h : list

        Returns
        -------
        int

        Examples
        --------
        >>> wer("who is there".split(), "is there".split())
        1
        >>> wer("who is there".split(), "".split())
        3
        >>> wer("".split(), "who is there".split())
        3
        """
        # initialisation
        d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint32)
        d = d.reshape((len(r)+1, len(h)+1))
        for i in range(len(r)+1):
            for j in range(len(h)+1):
                if i == 0:
                    d[0][j] = j
                elif j == 0:
                    d[i][0] = i

        # computation
        for i in range(1, len(r)+1):
            for j in range(1, len(h)+1):
                if r[i-1] == h[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    substitution = d[i-1][j-1] + 1
                    insertion    = d[i][j-1] + 1
                    deletion     = d[i-1][j] + 1
                    d[i][j] = min(substitution, insertion, deletion)

        return d[len(r)][len(h)]

    # Takes string instead of list for convenience
    @staticmethod
    def get_wer(trs, tts):
        trs = trs.split()
        tts = tts.split()

        assert(len(trs) <= (2**32)-1)
        assert(len(tts) <= (2**32)-1)

        return Articulation.wer(trs, tts)

    # Strips excess punctuation, converts to lower in order to offer a "fair" comparison
    @staticmethod
    def normalize(transcript):
        words = Articulation.get_words(transcript)
        return ' '.join(words).lower()

    # Conveniently reused from our text module
        # Only change: now removes "%HESITATION" that we get from text-to-speech
    @staticmethod
    def get_words(text):
        text = text.replace("%hesitation", "")
        text = text.translate({ ord(c): '' for c in "'\",.?!-:;="} )
        text = text.translate({ ord(c): ' ' for c in "\n"})
        words = text.split(' ')
        words = [w for w in words if len(w) > 0 and w != ' ']
        return words

    @staticmethod
    def test_wer():
        assert(Articulation.wer("test".split(), "test".split()) == 0)
        assert(Articulation.wer("cat".split(), "dog".split()) == 1)
        assert(Articulation.wer("cat".split(), "catdog".split()) == 1)
        assert(Articulation.wer("one".split(), "2 3 4 5".split()) == 4)

    # Takes in two strings to compare - trs: actual transcript | tts: text-to-speech
    # Returns word error rate divided by # of words in correct transcript (trs)
    @staticmethod
    def articulation(trs, tts):
        return Articulation.get_wer(trs, tts) / len(trs.split())


    # Disgustingly hacky way to scale our potentially unbounded word-error-rate to something that makes sense
        # If we get an articulation of 0 (meaning WER = 0), we had a perfect transcription.          So: art = 0  => 100%
        # We will arbitrarily set the boundary of "0% articulation" to mean WER >= len(trs.split()). So: art >= 1 => 0%
            # In other words, if we have an N word transcript and we need to perform >= N operations to make our text-to-speech match, then we consider this 0% articulation
        # Otherwise, our % will be 100 - (art * 100)                                                 So: 0 <= art < 1 => 100 - (art * 100)%

    # PRECONDITION: trs is the reference (correct) transcript given as a STRING, and tts is the text-to-speech transcript given as a STRING
    @staticmethod   
    def get_art_as_pct(trs, tts):
        trs_len = len(trs.split())
        wer = Articulation.get_wer(trs, tts)
        art = Articulation.articulation(trs, tts)


        if art >= 1:
            return 0
        else:
            return 100 * (1-art) # This covers both the "general case" (ie 0 < art < 1) and also the case where art == 0 implicitly
    
    @staticmethod
    def test_get_art_as_pct():
        assert(Articulation.get_art_as_pct("this is perfect", "this is perfect") == 100)
        assert(Articulation.get_art_as_pct("zeropercent", "so this result should totally give us 0 percent because art > 1") == 0)




    # optional unit quick unit tests
    #test_wer() 
    #test_get_art_as_pct()

    # Main execution
    @staticmethod
    def get_articulation(trs_path, tts_path):
        trs_path = "research/enigma_tc_transcript.txt"
        tts_path = "research/rkemper_take2_transcript_actual.txt"

        with open(trs_path, 'r', encoding='ascii', errors='ignore') as f:
            trs = unicodedata.normalize('NFKD', f.read())
            trs = Articulation.normalize(trs)

        with open(tts_path) as f:
            tts = f.read()
            tts = Articulation.normalize(tts)

        return Articulation.get_art_as_pct(trs, tts)



