import json
import os
# from  import filename

DATA_DIR="data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_data(filename,data):
    filepath=os.path.join(DATA_DIR,f"{filename}.json")
    with open(filepath,"w") as f:
        json.dump(data,f,indent=4)
    print(f"ma'lumot {filepath}ga saqlandi")


def load_data(filename):
    filepath = os.path.join( DATA_DIR, f"{filename}.json" )
    if not os.path.exists( filepath ):
        print( f"File {filepath} does not exist." )
        return None

    with open( filepath, 'r' ) as f:
        data = json.load( f )
    return data


def update_data(filename, new_data):
    existing_data = load_data( filename )
    if existing_data is None:
        print( "No existing data found. Creating new file." )
        save_data( filename, new_data )
        return

    if isinstance( existing_data, dict ):
        existing_data.update( new_data )
    elif isinstance( existing_data, list ):
        existing_data.extend( new_data )
    else:
        print( "Unsupported data format for updating." )
        return

    save_data( filename, existing_data )


def delete_data(filename):
    filepath = os.path.join( DATA_DIR, f"{filename}.json" )
    if os.path.exists( filepath ):
        os.remove( filepath )
        print( f"File {filepath} deleted." )
    else:
        print( f"File {filepath} does not exist." )


