"""Automation project File organizer and audit logger skipped and processed."""
import os
def automation_temp2():
    # getting the raw data
    raw_data = ["data.txt", "notes.txt", "image.png", "file.csv","report.txt","old.tmp"]
    processed_count = 0 #Defining the processed counts
    skipped_count = 0
    print("Mel, Were starting Automation!") #Announce the start
    for f in raw_data: #for (Storage of the "collected data" (f) ) to grab in raw_data:
        if f.endswith(".txt"): # if loop for conditions (Were getting files that ENDSWITH(".txt")
            clean_name = f.replace(".txt", "").upper() # This creates clean_name as a conversion for the data to be processed in
            print(f"Processing: {f} > {clean_name}") # processing: {f} = retrieved data > {conversion of that data}
            processed_count = processed_count + 1  #Adds 1 for processed_count for each data "cleaned"

            with open("log.txt", "a") as my_file: # Reminder: the "ink" to the pen = cleaning process
                my_file.write(f"clean_name: {clean_name}\n") # Writes the new data's in top to bottom format "\n"
        else:
            print(f"Skipping: {f} (Not a Text File)") # if the data doesnt contain .txt from the retrieved {stored data} = {f}
            skipped_count = skipped_count + 1 #Adds 1  for skipped_count after this function runs
    print("-"*30) #Visual Separator
    print(f"Task Complete , Final Summary") # Same as line 8 announces task complete
    print(f"Files Process: {processed_count}") #vvDisplays the counts {}vv
    print(f"Files Skipped!: {skipped_count}")

automation_temp2()