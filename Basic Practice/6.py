# A floppy disk shows 'f' bytes free and 'u' bytes used. If you delete a file of size 'o' bytes
# and create a new file of size 'n' bytes, how many free bytes will the floppy disk have?
# 'f u o and n' are user-entered value.

# f free
# u used
# o delete
# n new

f = int(input("Enter Free disk size in bytes..."))
u = int(input("Enter Used disk size in bytes..."))
o = int(input("Enter Old file size in bytes"))
n = int(input("Enter New file size in bytes"))

totalDiskSize = f+u
currentUsedDiskSize = u-o
currentUsedDiskSize = currentUsedDiskSize + n
currentFreeDiskSize = totalDiskSize - currentUsedDiskSize

print("Free Space Available", currentFreeDiskSize)
