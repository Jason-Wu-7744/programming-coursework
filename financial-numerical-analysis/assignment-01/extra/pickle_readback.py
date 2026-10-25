# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Alternative/practice version; the label does not imply original research.
import pickle
pkl_file = open('exercise-09_4.pkl', 'rb')
data1 = pickle.load(pkl_file)
print(data1)
pkl_file.close()