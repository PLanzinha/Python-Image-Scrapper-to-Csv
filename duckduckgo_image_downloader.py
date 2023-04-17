import DuckDuckGoImages as ddg


def image_downloader():
    user_input = input("Enter a query to search images for.\n")

    options = {
        # 'folder': '',  # The path where the downloaded images are saved. Default is current directory.
        'max_urls': 2,  # If set to a number, then only that amount of images will be downloaded.
        'thumbnails': False,  # Set to True if you want to download thumbnails instead.
        'parallel': True,  # Set to True for faster downloads using parallel processing.
        'shuffle': False,  # If set to true, the list of images will be shuffled randomly before download.
        'remove_folder': False,  # If set to true, the folder where the images will download to is deleted.
        'safe_search': False,  # If set to true it will make a search with "safe search" enabled.
        'license': ddg.ALL  # Change the license based on the license info below.
    }

    try:
        ddg.download(user_input, **options)
        print(f"Images on '{user_input}' downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    image_downloader()

# Licenses:
# ALL: retrieve all images, this is the default behaviour.
# CREATIVE_COMMONS: This will only retrieve images that have the Creative Commons licence.
# PUBLIC_DOMAIN: This will only retrieve images that are on the public domain.
# SHARE_AND_USE: This will only retrieve images that can be shared and used.
# SHARE_AND_USE_COMMERCIALLY: This will only retrieve images that can be shared and used commercially.
# MODIFY_SHARE_AND_USE: This will only retrieve images that can be modified, shared and used.
# MODIFY_SHARE_AND_USE_COMMERCIALLY: This will only retrieve images that can be modified, shared and used commercially.
