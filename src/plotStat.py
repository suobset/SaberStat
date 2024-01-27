import json
import matplotlib.pyplot as plt

def read_and_plot_json(file_path):
    timestamps = []
    rotation_rate_x = []
    rotation_rate_y = []
    rotation_rate_z = []

    with open(file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            payload = entry['payload'][0]  # Assuming there's only one payload in each entry

            timestamps.append(payload['time'])
            rotation_rate_x.append(payload['values']['rotationRateX'])
            rotation_rate_y.append(payload['values']['rotationRateY'])
            rotation_rate_z.append(payload['values']['rotationRateZ'])

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, rotation_rate_x, label='Rotation Rate X')
    plt.plot(timestamps, rotation_rate_y, label='Rotation Rate Y')
    plt.plot(timestamps, rotation_rate_z, label='Rotation Rate Z')

    plt.xlabel('Timestamp')
    plt.ylabel('Rotation Rate')
    plt.title('Wrist Motion Rotation Rates')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    json_file_path = 'path/to/your/log.json'
    read_and_plot_json(json_file_path)
