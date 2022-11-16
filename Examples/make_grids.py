from PIL import Image


def grid_images(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid
  
 
def prompt():
  try:
    prompt = input("Enter your Prompt:")
    if prompt == "":
      print("Prompt can't be empty")
      exit
    else:
      return prompt
  except:
    print("An unidentical Error occoured")
    exit()

def Generate_by_column(Prompt,rows,columns):
  all_images = []
  for i in range(rows):
    images = pipe(Prompt).images
    all_images.extend(images)

  grid_image = grid_images(all_images, rows=rows, cols=columns)
  display(grid_image)

def ImageCount():
  try:
    rows = int(input("Enter total number of Rows:"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return rows


def ImageCount():
  try:
    rows = int(input("Enter total number of Columns:"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return columns

def RowCount():
  try:
    row = int(input("Enter number of rows:"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return row

def ColumnCount():
  try:
    col = int(input("Enter number of Columns:"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return col


rows = RowCount()
columns = ColumnCount()
Text = prompt()
Prompt = [Text]*columns
Generate_by_column(Prompt,rows,columns)
