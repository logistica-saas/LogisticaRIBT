import sys
import shutil
from rembg import remove, new_session
from PIL import Image
import io

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        return

    input_path = sys.argv[1]
    output_path = "output.png"

    with open(input_path, "rb") as input_file:
        input_data = input_file.read()

    try:
        session = new_session("isnet-general-use")

        result = remove(
            input_data,
            session=session,
            alpha_matting=False,
            only_mask=False,
            post_process_mask=False
        )

        with open(output_path, "wb") as output_file:
            output_file.write(result)

        print(f"Transparent background saved to {output_path}")
    except Exception as e:
        print(f"Background removal failed: {e}\nUsing original image instead.")
        shutil.copy(input_path, output_path)
        print(f"Original image copied to {output_path}")

if __name__ == "__main__":
    main()
