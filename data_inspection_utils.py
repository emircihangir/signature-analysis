import matplotlib.pyplot as plt
import io
from PIL import Image

def plots_to_gif(x_values, y_values, batch:tuple[int,int], file_name="inspection_output"):
    pil_images = []

    for i in range(batch[0], batch[1]):
        arb_sample = x_values[i]

        arb_sample_x = arb_sample[:, 0]
        arb_sample_y = arb_sample[:, 1]
        arb_sample_z = arb_sample[:, 2]

        # filter zero values caused by normalization
        # arb_sample_x = arb_sample_x[arb_sample_x != 0]
        # arb_sample_y = arb_sample_y[arb_sample_y != 0]
        # arb_sample_z = arb_sample_z[:len(arb_sample_x)]

        plt.figure(figsize=(10,8))
        plt.text(0.5, 0, f'#{i}, label={y_values[i]}', ha='center', va='bottom', transform=plt.axes().transAxes, fontsize=10)
        plt.axis('off')
        scatter = plt.scatter(arb_sample_x, arb_sample_y * -1, s=300, c = arb_sample_z, cmap='viridis')
        cbar = plt.colorbar(scatter)
        cbar.set_label('timestamp')

        print(f'\rCompleted image #{i:04}', end='', flush=True)

        # Convert figure to PIL Image
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img = Image.open(buf)
        pil_images.append(img)
        plt.close()

    pil_images[0].save(f"{file_name}_{batch[0]}-{batch[1]-1}.gif", format='GIF',
                append_images=pil_images[1:],
                save_all=True,
                duration=100,
                loop=0)

def plot_sample(input_value, label_value, k=1, plot_dpi=100):
    """
    set k = -1 to invert the plot
    """
    input_value_x = input_value[:, 0]
    input_value_y = input_value[:, 1]
    input_value_z = input_value[:, 2]
    
    plt.figure(figsize=(10,8), dpi=plot_dpi)
    plt.text(0.5, 0, f'label={label_value}', ha='center', va='bottom', transform=plt.axes().transAxes, fontsize=10)
    # plt.axis('off')
    scatter = plt.scatter(input_value_x, input_value_y * k, s=300, c = input_value_z, cmap='viridis')
    cbar = plt.colorbar(scatter)
    cbar.set_label('timestamp')