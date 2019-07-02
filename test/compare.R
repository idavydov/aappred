library(e1071)

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

props.train <- read.table('../svm/props.train')
props.Y <- props.train$V1
props.X <- as.matrix(props.train[-1])

model <- svm(props.X, props.Y, scale=FALSE, type='C-classification',
             kernel='radial', gamma=8, cost=4, tolerance=1e-6,
             shrinking=TRUE)


test.X <- as.matrix(read.table('long_features.txt'))
test.pred <- predict(model, test.X, decision.values=TRUE)

summary(attr(test.pred, "decision.values") - ref.pred$svm1)
## Min.   :-0.0032035
## 1st Qu.:-0.0007867
## Median :-0.0004117
## Mean   :-0.0004277
## 3rd Qu.:-0.0000666
## Max.   : 0.0031650

## results are the same, no surprise since it is using libsvm
