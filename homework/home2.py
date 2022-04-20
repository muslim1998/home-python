from pathlib import Path

Path("file3").write_text(Path("file_1").read_text() + 
                         Path("file_2").read_text())









# import glob
# files = glob.glob( '*.txt' )

# with open( 'result.txt', 'w' ) as result:
#     for file_ in files:
#         for line in open( file_, 'r' ):
#             result.write(line)