# Set WD
setwd("~/Dropbox/Varoon_Files/Varoon's School Folder/3 - Berkeley/Term 1/CYBER 202/Assignments/Final Project/DNA Cryptography/Alg Implementation/Ready for Analysis/Round Functions")

# PLOT SET 1

hist_1 <- read_csv("hist_1.csv", col_names = c("char", "freq")) %>% 
  mutate(num_round_functions = 1)
hist_10 <- read_csv("hist_10.csv", col_names = c("char", "freq")) %>% 
  mutate(num_round_functions = 10)
hist_100 <- read_csv("hist_100.csv", col_names = c("char", "freq")) %>% 
  mutate(num_round_functions = 100)

combined_hist_df <- 
  rbind.data.frame(hist_1, hist_10, hist_100) %>% 
  left_join(color_df)

hist_fills = c("#1C8F63", "#CD4A06", "#6259A3")

text_df <- read_csv("text_df.csv")

text_annotations_df <- combined_hist_df %>% 
  left_join(text_df) %>% 
  select(num_round_functions, ess) %>% 
  unique() %>% 
  mutate(ess_est = paste(expression(ess), "≈", round(ess, 4)))

plot_set_1 <- 
  combined_hist_df %>% 
  ggplot(aes(x = char, y = freq)) +
  geom_bar(aes(fill = colors), stat = "identity") +
  facet_wrap(. ~ num_round_functions, ncol = 1)  +
  scale_fill_manual(values = hist_fills,
                    guide = "none") +
  theme_gray() + 
  ggtitle("Ciphertext Characters by Round Function Count\nPlaintext = 'A' x 100\n") +
  xlab("Cipher Text Character") +
  ylab("Count") + 
  geom_text(data = text_annotations_df, 
            aes(x = 24, y = 18, label = ess_est))

# PLOT SET 2

round_function_sds <-
  list.files(pattern = "round_function_analysis") %>% 
  map_df(~read_csv(.))


# color table
num_round_functions = as.numeric(c(1, 10, 100))
colors = c("#1C8F63", "#CD4A06", "#6259A3")
color_df = cbind.data.frame(num_round_functions, colors)

hist_fills = c("#1C8F63", "#CD4A06", "#6259A3")

plot_set_2 <- round_function_sds %>%
  left_join(color_df) %>%  
  group_by(num_round_functions) %>% 
  mutate(lower = quantile(encryption_strenth_score, 0.025),
         upper = quantile(encryption_strenth_score, 0.975)) %>% 
  ungroup() %>% 
  ggplot(aes(x = encryption_strenth_score)) +
  geom_histogram(aes(fill = colors)) +
  facet_wrap(. ~ num_round_functions, ncol = 1)  +
  scale_fill_manual(values = hist_fills,
                    guide = "none") +
  geom_vline(aes(xintercept = lower)) +
  geom_vline(aes(xintercept = upper)) +
  ggtitle("Distribution of Encryption Strength Scores\nby Round Function Count\n100 Randomly Selected English Words; n = 1,000") +
  xlab("Encryption Strength Score") +
  ylab("Frequency") +
  theme_gray() +
  scale_x_continuous(labels = scales::number_format(accuracy = 0.0001))




# PUTTING THEM TOGETHER
grid.arrange(plot_set_1,
             plot_set_2, ncol = 2)


  
  