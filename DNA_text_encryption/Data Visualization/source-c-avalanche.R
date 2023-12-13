# Source C Avalance

source_c_avalanche <- read.csv("~/Dropbox/Varoon_Files/Varoon's School Folder/3 - Berkeley/Term 1/CYBER 202/Assignments/Final Project/DNA Cryptography/Alg Implementation/Ready for Analysis/Avalance Effect/source_c_avalanche.csv")

source_c_avalanche %>% 
  ggplot(aes(x = bits_changed, y = pct_ciphertext_change)) +
  geom_point(col = "purple") +
  geom_line(col = "purple") +
  theme_gray() +
  xlab("Number of Bits Changed in Key") +
  ylab("Avalanche Effect") +
  ggtitle("Avalance Effect vs. Number of Bits Changed (Pavithran)") +
  scale_y_continuous(labels = scales::percent)


 