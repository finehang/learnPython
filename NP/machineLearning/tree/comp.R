age <- c("young", "middle", "old")
income <- c("high", "medium", "low")
student <- c("yes", "no")
credit <- c("good", "normal")
buy <- c("yes", "no")


addData <- function(){
  return (tibble(age = sample(age, 1), income = sample(income, 1), stuent = sample(student, 1), 
                credit = sample(credit, 1), buy = sample(buy, 1)))
}

for(i in 1:100){
  x <- x %>% add_row(addData())
}

write_csv(x, "./comp.csv")
