from Video import VideoAnalysis

class Interface:

    def process_filepath(self, file_path, options):
        challenge_id = options['challenge_id']

        if challenge_id is None:
            print("ERROR: No challenge_id provided. Exiting\n")
            return -1   
            
        sentiment = False
        coords = False
        vid_analysis = VideoAnalysis(file_path)
        for(opt, val) in options.items():

            if val:
                if opt == "run_all":
                    sentiment = True
                    coords = True
                    break
                elif opt == "sentiment":
                    sentiment = True
                elif coords == "coords":
                    coords = True
                else:
                    print("ERROR: Options are {run_all, sentiment, coords}")
                    exit(1)

        results = {}
        if sentiment:
            sentiment = vid_analysis.get_sentiment()
            results["sentiment_and_time"] = sentiment

        if coords:
            coords = vid_analysis.get_coords()
            results["coords_and_time"] = coords

       
        return results
