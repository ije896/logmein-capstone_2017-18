import VideoAnalysis
import json
import sys

def process_filepath(file_path, options):
    sentiment = False
    coords = False
    vid_analysis = VideoAnalysis.VideoAnalysis(file_path)

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

    json_list = {}
    if sentiment:
        sentiment = vid_analysis.get_sentiment()
        json_list["sentiment_and_time"] = sentiment

    if coords:
        coords = vid_analysis.get_coords()
        json_list["coords_and_time"] = coords

    json_obj = json.dumps(json_list, indent=2)
    # print(json_obj)
    return json_list

def main():
    process_filepath(sys.argv[1], {"run_all" : True})

if __name__ == '__main__':
    main()
