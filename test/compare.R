ref.pred <- read.table('long_reference.txt', col.names=c('n', 'aa', 'svm1', 'svm2'))
cur.pred <- read.table('long.txt', col.names=c('n', 'aa', 'svm1', 'svm2'))

str(ref.pred)
str(cur.pred)

summary(ref.pred$svm1 - cur.pred$svm1)
##       Min.    1st Qu.     Median       Mean    3rd Qu.       Max.
## -0.0031680  0.0000660  0.0004120  0.0004281  0.0007880  0.0032070

summary(ref.pred$svm2 - cur.pred$svm2)
##      Min.   1st Qu.    Median      Mean   3rd Qu.      Max.
## -1.80e-05 -7.00e-06  0.00e+00 -4.13e-07  6.00e-06  1.80e-05
