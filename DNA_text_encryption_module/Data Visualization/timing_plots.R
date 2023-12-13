# Set WD
setwd("~/Dropbox/Varoon_Files/Varoon's School Folder/3 - Berkeley/Term 1/CYBER 202/Assignments/Final Project/DNA Cryptography/Alg Implementation/Ready for Analysis/Timings/Final")

# Libraries
library(data.table)
library(gridExtra)
library(latex2exp)
library(tidyverse)
library(reshape2)

##############
# Encryption and Decryption Timing Plots
#############

timings_df <-
  list.files(pattern = "\\.csv$") %>% 
  map_df(~read_csv(.)) %>% 
  mutate(alg_run = recode(alg_run, `source_b` = "Ubaidur", 
                          `source_c` = "Pavithran",
                          `source_e` = "Hazra")) %>% 
  gather("encryption_time", "decryption_time",
         key = "operation", value = time) %>% 
  mutate(num_words = factor(num_words, ordered = TRUE,
                            levels = seq(100, 2000, 100))) %>% 
  mutate(operation = recode(operation, `encryption_time` = "Encryption", 
                          `decryption_time` = "Decryption",
                          `source_e` = "Hazra")) %>% 
  mutate(operation = factor(operation, ordered = TRUE, 
                            levels = c("Encryption", "Decryption")))
  
  

plot_individual_alg_timings <- function(alg_of_choice) {

  timings_df %>% 
  filter(alg_run == alg_of_choice) %>% 
  filter(num_words < 1600) %>% 
  ggplot(aes(x = num_words, y = time, fill = operation)) +
  geom_boxplot() +   
  scale_fill_discrete(name = "") +
  theme_linedraw() +
  xlab("Input Size (number of words)") +
  ylab("Time (sec.)") +
  ggtitle(paste(paste0(alg_of_choice, " Algorithm:"), "Time vs. Input Size"))
  
}

plot_individual_alg_timings(alg_of_choice = "Ubaidur")
plot_individual_alg_timings(alg_of_choice = "Pavithran")
plot_individual_alg_timings(alg_of_choice = "Hazra")

# grid, one graph for each alg and operation combo
timings_df %>% 
  filter(num_words < 1600) %>% 
  ggplot(aes(x = num_words, y = time, fill = alg_run)) +
  geom_boxplot() +
  facet_wrap(operation ~ alg_run, scales = "free_y") +
  theme_linedraw() + 
  scale_fill_discrete(name = "Algorithm") +
  scale_x_discrete(breaks = as.character(seq(0, 1600, 200)))
# What's interesting about these graphs is that the rates of timing change over
# the input size appear approximately equal across all algs and operations
  
# grid, one graph for each alg
timings_df %>% 
  filter(num_words < 1600) %>% 
  ggplot(aes(x = num_words, y = time, fill = operation)) +
  geom_boxplot() +
  facet_wrap(. ~ alg_run, scales = "free_y", nc = 1) +
  theme_gray() + 
  scale_fill_brewer(type = "qual", palette = 4, direction = 1, aesthetics = "fill",
                    name = "") + 
  scale_x_discrete(breaks = as.character(seq(0, 1600, 200))) +
  xlab("Input Length (number of words)") +
  ylab("Time (sec.)") +
  ggtitle("Time vs. Input Size by Algorithm and Operation") 
# SHOW 1
# Very interesting, show this plot
# Hazra - Decryption and Encryption are roughly comparable over the input space
# Pavithrana - Encryption faster than decryption at longer inputs
# Ubaidur - Decryption is faster than encryption at longer inputs


timings_df %>% 
  filter(num_words < 1600) %>% 
  filter(alg_run != "Ubaidur") %>% 
  ggplot(aes(x = num_words, y = time, fill = alg_run)) +
  geom_boxplot() +
  facet_wrap(operation ~.) +
  theme_gray() + 
  scale_fill_brewer(palette = "Dark2", name = "Algorithm") + 
  scale_x_discrete(breaks = as.character(seq(0, 1600, 200))) +
  xlab("Input Length (number of words)") +
  ylab("Time (sec.)") +
  ggtitle("Hazra vs. Pavithran Encryption and Decryption Times") 
# SHOW 2
# Hazra vs. Pavithrana...
# Encryption times are very close to one another
# But the grpah shows advantages of Hazra's decryption speeds...market divergence
# in decryption times compared to encryption, which are much tighter


# Findings limits...median time 
median_timings_df <- timings_df %>% 
  group_by(alg_run, num_words, operation) %>% 
  summarise(median_time = median(time))

median_timings_df %>% 
  filter(num_words == 1000) %>% View()

median_timings_df %>% 
  ggplot(aes(x = num_words, y = median_time, color = alg_run)) +
  geom_point() +
  facet_grid(. ~ operation, scales = "free_y")

# Trying to show heteroskedasticity plot
median_timings_df %>% 
  spread(operation, median_time) %>% 
  group_by(alg_run, num_words) %>% 
  summarise(decryption_ratio = Decryption / Encryption) %>% 
  ungroup() %>% 
  filter(num_words < 1600) %>% 
  ggplot(aes(x = num_words, y = decryption_ratio, col = alg_run, group = alg_run)) +
  geom_line() +
  xlab("Input Length (number of words)") +
  ylab("Decryption Ratio = Decryption Time / Encryption Time") +
  ggtitle("Variable Time Execution: Decryption Ratios vs. Input Length by Algorithm") +
  scale_color_discrete(name = "Algorithm") +
  geom_hline(yintercept =  1, linetype = "dotted")
  
  

# ### Archived Code
# 
# %>% 
#   mutate(num_words = factor(num_words, ordered = TRUE, 
#                             levels = c(50, 100, 200, 300, 400, 500, 
#                                        600, 700, 800, 900, 1000)))
# 
# level_order <- c(50, seq(100, 1000, 100))
# 
# timing_df_10_rd %>% 
#   ggplot(aes(x = factor(num_words, levels = level_order),  
#              y = time, fill = operation)) +
#   geom_boxplot() +
#   xlab("Input Size (number of words)") +
#   ylab("Time (sec.)") +
#   ggtitle("Encryption and Decryption Times vs. Input Size") +
#   theme_linedraw() +
#   scale_fill_discrete(name = "", labels = c("Decryption", "Encryption"))
# 
# 
# ###### Graph for 100 Rounds
# setwd("~/Dropbox/Varoon_Files/Varoon's School Folder/3 - Berkeley/Term 1/CYBER 202/Assignments/Final Project/DNA Cryptography/Alg Implementation/Ready for Analysis/Timings/100 Round Functions")
# 
# timing_df_100_rd <-
#   list.files(pattern = "\\.csv$") %>% 
#   map_df(~read_csv(.)) %>% 
#   mutate(rd_functions = "100 Round Functions") %>% 
#   gather("encryption_time", "decryption_time", key = "operation", value = time) %>% 
#   mutate(num_words = factor(num_words, ordered = TRUE, 
#                             levels = c(50, 100, 200, 300, 400, 500, 
#                                        600, 700, 800, 900, 1000)))
# 
# timing_df_100_rd %>% 
#   ggplot(aes(x = factor(num_words, levels = level_order),  
#              y = time, fill = operation)) +
#   geom_boxplot() +
#   xlab("Input Size (number of words)") +
#   ylab("Time (sec.)") +
#   ggtitle("Encryption and Decryption Times vs. Input Size") +
#   theme_linedraw() +
#   scale_fill_discrete(name = "", labels = c("Decryption", "Encryption"))
# 
# timing_df <- rbind.data.frame(timing_df_10_rd,
#                               timing_df_100_rd)
# 
# timing_df %>% 
#   filter(rd_functions == "10 Round Functions") %>%
#   ggplot(aes(x = factor(num_words, levels = level_order),  
#              y = time, fill = operation)) +
#   geom_boxplot() +
#   xlab("Input Size (number of words)") +
#   ylab("Time (sec.)") +
#   ggtitle("Encryption and Decryption Times vs. Input Size") +
#   theme_linedraw() +
#   scale_fill_discrete(name = "", labels = c("Decryption", "Encryption")) +
#   facet_wrap(.~rd_functions)
# # facet_grid(rd_functions ~ ., scales = "free_y")
# 
# 
