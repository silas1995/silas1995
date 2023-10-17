data <- data.frame(date = sample(seq(as.Date("2020/01/01"),
                                     by = "day",
                                     length.out = 1000),
                                 100, replace = TRUE),
                   value = round(rnorm(100, 5, 2), 2))
View(data)

#Aggregate Daily Data to Month/Year Intervals Using Base R
# Create year column
data$year <- strftime(data$date, "%Y") 
# Create month colum
data$month <- strftime(data$date, "%m")  

# Aggregate data
data_aggr1 <- aggregate(value ~ month + year,     
                        data,
                        FUN = sum)
Kisii_T5$Year <- strftime(Kisii_T5$Date, "%Y")
# Create month colum
Kisii_T5$Month <- strftime(Kisii_T5$Date, "%m")

# Aggregate data
Kisii_T5_msum <- aggregate(Kisii_T5 ~ Month + Year,     
                        Kisii_T5,
                        FUN = sum)
Kisii_T5_msum
plot(Kisii_T5_msum$Kisii_T5~Kisii_T5_msum$Month,type='lm')
