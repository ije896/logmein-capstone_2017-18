from Video import VideoAnalysis
import json

class Interface:

    @staticmethod
    def process_filepath(file_path, options):
        challenge_id = options['challenge_id']

        if challenge_id is None:
            print("ERROR: No challenge_id provided. Exiting\n")
            return -1

        # TODO: decide if challenge_id determines which metrics we provide

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

        json_list = []
        if sentiment:
            sentiment = vid_analysis.get_sentiment()
            json_list.append(sentiment)

        if coords:
            coords = vid_analysis.get_coords()
            json_list.append(coords)

        json_obj = json.dumps(json_list, indent=2)
        return json_obj
