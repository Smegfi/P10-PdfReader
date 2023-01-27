import zalohovac
import application
from datetime import datetime

start = datetime.now()
zalohovac.MoveFiles()
zalohovac.CleanBackup()

application.ConvertToImage()

end = datetime.now()

dif = end - start
print(dif)