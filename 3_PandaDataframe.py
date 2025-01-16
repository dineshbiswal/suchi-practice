import pandas as pd
a={"day":["d1","d2","d3"],"dur":[10,20,30]}
b=pd.DataFrame(a)
print(b)

import pandas as pd
a={"day":["d1","d2","d3"],"dur":[10,20,30]}
b=pd.DataFrame(a,index=["x","y","z"])
print(b.loc[["x","y"]])