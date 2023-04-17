import os
from bing_image_downloader import downloader


class EnhancedBingImageDownloader:
    def __init__(self, query_string, limit=10, output_dir='download', adult_filter_off=True, force_replace=True,
                 timeout=60, filter_type="", verbose=True):
        self.query_string = query_string
        self.limit = limit
        self.output_dir = output_dir
        self.adult_filter_off = adult_filter_off
        self.force_replace = force_replace
        self.timeout = timeout
        self.filter_type = filter_type
        self.verbose = verbose

    def download_images(self):
        downloader.download(
            self.query_string,
            limit=self.limit,
            output_dir=self.output_dir,
            adult_filter_off=self.adult_filter_off,
            force_replace=self.force_replace,
            timeout=self.timeout,
            filter=self.filter_type,
            verbose=self.verbose
        )

    def create_output_directory(self):
        input_name_folder = os.path.join(self.output_dir, self.query_string)

        if not os.path.exists(input_name_folder) or self.force_replace:
            os.makedirs(input_name_folder, exist_ok=True)
        else:
            print(f"Folder '{input_name_folder}' already exists.")

    def get_user_input(self):
        user_image_limit = input("Enter the limit number of images downloaded.\n")
        if user_image_limit.isdigit():
            self.limit = int(user_image_limit)
        else:
            print("Invalid input. Using the default limit of 10 images.")

    def run(self):
        self.get_user_input()
        self.create_output_directory()
        self.download_images()


if __name__ == "__main__":
    user_input = input("Enter a query to search images for.\n")
    image_downloader = EnhancedBingImageDownloader(user_input, limit=10, output_dir='download',
                                                   adult_filter_off=True, force_replace=False, timeout=60,
                                                   filter_type="photo", verbose=True)
    image_downloader.run()
