from pycocotools.coco import COCO
import requests

coco = COCO('./filtered2.json')
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]

catIds = coco.getCatIds(catNms=['person'])
imgIds = coco.getImgIds(catIds=catIds )
images = coco.loadImgs(imgIds)

for im in images:
#print("im: ", im)
  img_data = requests.get(im['coco_url']).content
  with open('COCO/' + im['file_name'], 'wb') as handler:
    handler.write(img_data)
