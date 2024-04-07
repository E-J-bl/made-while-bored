from central import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    store=Storage(100)# change this to change the natural balacing point
    store.run()
    print(f"you have a final storage system of \n{store.storage},\nand you took out\n{store.outtake}\n")
