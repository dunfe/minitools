# Set your Cloudinary credentials
# ==============================
import urllib

from dotenv import load_dotenv

load_dotenv()

# Import the Cloudinary libraries
# ==============================
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Import to format the JSON responses
# ==============================
import json

# Set configuration parameter: return "https" URLs by setting secure=True
# ==============================
config = cloudinary.config(secure=True)

# Log the configuration
# ==============================
print(
    "****1. Set up and configure the SDK:****\nCredentials: ",
    config.cloud_name,
    config.api_key,
    "\n",
)


def upload_image():

    # Upload the image and get its URL
    # ==============================

    # Upload the image.
    # Set the asset's public ID and allow overwriting the asset with new versions
    cloudinary.uploader.upload(
        "logo.png", public_id="infiniplanet_logo", unique_filename=False, overwrite=True
    )

    # Build the URL for the image and save it in the variable 'srcURL'
    src_url = cloudinary.CloudinaryImage("infiniplanet_logo").build_url(
        transformation=[
            {"width": 150, "height": 150, "crop": "fill"},
        ],
    )

    # Log the image URL to the console.
    # Copy this URL in a browser tab to generate the image on the fly.
    print("****2. Upload an image****\nDelivery URL: ", src_url, "\n")


def main():
    upload_image()


main()
