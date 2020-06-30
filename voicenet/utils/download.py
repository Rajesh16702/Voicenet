import os
import wget
import tarfile


def extract_dataset(compressed_dataset_file_name, dataset_directory):
        try:
            tar = tarfile.open(compressed_dataset_file_name, "r:gz")
            tar.extractall(dataset_directory)
            tar.close()
            print("Files extraction was successful!")

        except:
            print("No extraction was performed !")


def download_staeds_extract_data(direc= "."):
    """
    Download ST American English Speech data

    Parameters
    ----------
    dir: str
        Directory where the dataset will be stored

    """

    direc = os.path.expanduser(direc)

    if not os.path.exists(direc):
        os.makedirs(direc)

    # Download SQuAD 1.1
    print("Downloading ST American English Corpus...")

    data_url = 'https://github.com/Robofied/Voicenet/releases/download/v1.0/ST-AEDS-20180100_1-OS.tgz'
    
    file = data_url.split("/")[-1]
    if os.path.exists(os.path.join(direc, file)):
        print(file, "already downloaded")
    else:
        wget.download(url=data_url, out=direc)
        dataset_dir = os.path.join(direc, 'ST-AEDS')
        extract_dataset(file, dataset_dir)
        
    



# wget.download(url='https://github.com/Robofied/Voicenet/releases/download/v1.0/ST-AEDS-20180100_1-OS.tgz', out='.')

    