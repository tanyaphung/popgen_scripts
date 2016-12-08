args<-commandArgs(TRUE)

X_data <- read.table(args[1], header=FALSE)
A_data <- read.table(args[2], header=FALSE)

X_meanReadDepth=mean(X_data[,3])/mean(X_data[,2])
A_meanReadDepth=mean(A_data[,3])/mean(A_data[,2])

X_A_ratio <- X_meanReadDepth/A_meanReadDepth

print (X_meanReadDepth)
print (A_meanReadDepth)
print (X_A_ratio)

if (abs(0.5-X_A_ratio) < abs(1-X_A_ratio)){
	print ("Male")
} else {
	print ("Female")
}
