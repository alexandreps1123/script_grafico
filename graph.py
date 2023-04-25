import matplotlib.pyplot as plt
import json, sys

def read_json_file(argv):
    f = open(argv)
    data = json.load(f)
  
    f.close()
    return data

def plot_line_chart(json_data):
    coverage_directed_greybox_y_percent = []
    coverage_greybox_y_percent = []
    titles = []
    datas = []

    for i in json_data:
        titles.append(i)
        datas.append(dict(json_data[i]))

    for (data, title) in zip(datas, titles):
        coverage_directed_greybox_y_percent.clear()
        coverage_greybox_y_percent.clear()

        fig, axs = plt.subplots(2, 2)
        fig.suptitle(title)

        # directed_greybox
        # coverage
        coverage_directed_greybox_x = data["directed_greybox"][0]["execution"]["coverageByTime"]["x"]
        coverage_directed_greybox_y = data["directed_greybox"][0]["execution"]["coverageByTime"]["y"]
        
        # distance
        distance_directed_greybox_x = data["directed_greybox"][0]["execution"]["minDistanceByTime"]["x"]
        distance_directed_greybox_y = data["directed_greybox"][0]["execution"]["minDistanceByTime"]["y"]

        # greybox
        # coverage
        coverage_greybox_x = data["greybox"][0]["execution"]["coverageByTime"]["x"]
        coverage_greybox_y = data["greybox"][0]["execution"]["coverageByTime"]["y"]
        
        # distance
        distance_greybox_x = data["greybox"][0]["execution"]["minDistanceByTime"]["x"]
        distance_greybox_y = data["greybox"][0]["execution"]["minDistanceByTime"]["y"]

        # total directed_greybox
        total_instructions_directed_greybox = data["directed_greybox"][0]["execution"]["totalInstructions"]

        # total greybox
        total_instructions_greybox = data["greybox"][0]["execution"]["totalInstructions"]

        # percentage coverage directed greybox y
        for i in coverage_directed_greybox_y:
            coverage_directed_greybox_y_percent.append(i / total_instructions_directed_greybox * 100)

        # percentage coverage greybox y
        for i in coverage_greybox_y:
            coverage_greybox_y_percent.append(i / total_instructions_greybox * 100)

        # directed_greybox
        axs[0, 0].plot(coverage_directed_greybox_x, coverage_directed_greybox_y_percent)
        axs[0, 0].set_xticks([0, len(coverage_directed_greybox_x)-1])
        #plt.xticks(rotation=45)
        axs[0, 0].set_title('Coverage By Time')

        axs[1, 0].plot(distance_directed_greybox_x, distance_directed_greybox_y)
        axs[1, 0].set_xticks([0, len(distance_directed_greybox_x)-1])
        axs[1, 0].set_title('Min Distance By Time')

        # greybox
        axs[0, 1].plot(coverage_greybox_x, coverage_greybox_y_percent)
        axs[0, 1].set_xticks([0, len(coverage_greybox_x)-1])
        axs[0, 1].set_title('Coverage By Time')

        
        axs[1, 1].plot(distance_greybox_x, distance_greybox_y)
        axs[1, 1].set_xticks([0, len(distance_greybox_x)-1])
        axs[1, 1].set_title('Min Distance By Time')

        plt.show()


    # print("\n\n\n")
    # print(data[0]["directed_greybox"])

    # directed_greybox
    # coverage_directed_x = data[0][0]["execution"]["coverageByTime"]["x"]
    # coverage_directed_y = data[0][0]["execution"]["coverageByTime"]["y"]
    
    # distance_directed_x = data[0][0]["execution"]["minDistanceByTime"]["x"]
    # distance_directed_y = data[0][0]["execution"]["minDistanceByTime"]["y"]

    # outro_metodo
    # x1 = data["directed_greybox"][0]["execution"]["minDistanceByTime"]["x"]
    # y1 = data["directed_greybox"][0]["execution"]["minDistanceByTime"]["y"]
    

    # totalInstructions = data["directed_greybox"][0]["execution"]["totalInstructions"]
    
    # for i in y:
    #     y_list.append(i / totalInstructions * 100)
   

    # fig, axs = plt.subplots(2, 2)
    # fig.suptitle("CBToken.sol")
    # axs[0, 0].plot(coverage_directed_x, coverage_directed_y)
    # axs[0, 0].set_xticks([0, len(coverage_directed_x)/2, len(coverage_directed_x)-1])
    # plt.xticks(rotation=45)
    # axs[0, 0].set_title('Coverage By Time')

    # axs[1, 0].plot(distance_directed_x, distance_directed_y)
    # axs[1, 0].set_title('Min Distance By Time')

    # axs[0, 1].plot(x1, y1)
    # axs[0, 1].set_title('Coverage By Time')

    
    
    # axs[1, 1].plot(x1, y1)
    # axs[1, 1].set_title('Min Distance By Time')

    # y = x["startTime"]

    # if False:
    #     for i in y:
    #         y_axis.append(i / json_data['totalInstructions'] * 100)
    # else:
    #     y_axis = y

    # fig, axs = plt.subplots(2, 2)
    # fig.suptitle('Vertically stacked subplots')
    # axs[0, 0].plot(x, y)
    # axs[0, 1].plot(x, y)
    # axs[1, 0].plot(x, y)
    # axs[1, 1].plot(x, y)

    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.plot(x_axis, y_axis)
    # ax.set_aspect(aspect=1)
    # ax.cla()
    # plt.xticks(rotation=45)
    # plt.show()


if __name__ == "__main__":
    json_data = read_json_file(sys.argv[1])
    plot_line_chart(json_data)
    # plot_line_chart(json_data, 'minDistanceByTime', 'Min Distance By Time','x', 'y', False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
