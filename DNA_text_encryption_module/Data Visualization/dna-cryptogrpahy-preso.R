# These plots were made (but not presented due to a lack of time) to show the logic
# behind the encryption strength score.

# Set WD
setwd("~/Dropbox/Varoon_Files/Varoon's School Folder/3 - Berkeley/Term 1/CYBER 202/Assignments/Final Project/DNA Cryptography/Presentation")

characs <-  c("B", "C", "D", "E", "F", "G", "H", "I")
set_1 <- c(0, 0, 0, 8, 0, 0, 0, 0) 
set_2 <- c(0, 0, 2, 4, 2, 0, 0, 0) 
set_3 <- c(0, 2, 2, 0, 2, 2, 0, 0) 
set_4 <- c(1, 1, 1, 1, 1, 1, 1, 1) 

toy_df <- cbind.data.frame(
  characs,
  set_1, 
  set_2,
  set_3, 
  set_4) %>% 
  gather("set_1", "set_2", "set_3", "set_4", key = "alg", value = "freq")

toy_df %>% 
  mutate(alg = recode(alg, 
                      `set_1` = "Algorithm 1", 
                      `set_2` = "Algorithm 2",
                      `set_3` = "Algorithm 3",
                      `set_4` = "Algorithm 4")) %>% 
  # filter(alg == "Algorithm 2") %>% 
  ggplot(aes(x = characs, y = freq, fill = alg)) +
  geom_bar(stat = "identity")+
  theme_linedraw() +
  scale_fill_brewer(palette = "Dark2", guide = "none") +
  facet_wrap(alg~.) +
  xlab("Ciphertext Character") +
  ylab("Frequency") + 
  geom_hline(yintercept = 1, linetype = "dashed") 



characs <-  c("B", "C", "D", "E", "F", "G", "H", "I")
set_5 <- c(0, 2, 0, 3, 0, 1, 0, 2) 
set_6 <- c(0, 2, 0, 2, 0, 2, 0, 2) 

toy_df2 <- cbind.data.frame(
  characs,
  set_5,
  set_6)

toy_df2 %>% 
  gather("set_5", "set_6", key = "alg", value = "freq") %>% 
  mutate(alg = recode(alg, 
                      `set_5` = "Algorithm 5", 
                      `set_6` = "Algorithm 6")) %>% 
  ggplot(aes(x = characs, y = freq, fill = alg)) +
  geom_bar(stat = "identity")+
  theme_linedraw() +
  scale_fill_brewer(palette = "Set2", guide = "none") +
  facet_wrap(alg~., nr = 1) +
  xlab("Ciphertext Character") +
  ylab("Frequency") + 
  geom_hline(yintercept = 1, linetype = "dashed") 