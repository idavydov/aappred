ref.pred <- read.table('long_reference.txt', col.names=c('n', 'aa', 'svm1', 'svm2'))
cur.pred <- read.table('long.txt', col.names=c('n', 'aa', 'svm1', 'svm2'))

str(ref.pred)
str(cur.pred)

summary(ref.pred$svm1 - cur.pred$svm1)
##      Min.    1st Qu.     Median       Mean    3rd Qu.       Max.
## -0.0052290  0.0001190  0.0007360  0.0007193  0.0013510  0.0048440

summary(ref.pred$svm2 - cur.pred$svm2)
##      Min.   1st Qu.    Median      Mean   3rd Qu.      Max.
## -1.80e-05 -7.00e-06  0.00e+00 -4.13e-07  6.00e-06  1.80e-05
