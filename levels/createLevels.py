import pickle

lvl_file = open("new.lvl", "wb")

lvls = [([(212, 100), (412, 100), (612, 100), (812, 100),
		  (112, 200), (312, 200), (512, 200), (712, 200), (912, 200),
		  (212, 300), (412, 300), (612, 300), (812, 300)], 100, 500),
		([(112, 100), (312, 100), (512, 100), (712, 100), (912, 100),
		  (212, 200), (412, 200), (612, 200), (812, 200),
		  (112, 300), (312, 300), (512, 300), (712, 300), (912, 300)], 100, 500),
		([(112, 100), (212, 100), (312, 100), (412, 100), (512, 100), (612, 100), (712, 100), (812, 100), (912, 100),
		  (112, 200), (212, 200), (312, 200), (412, 200), (512, 200), (612, 200), (712, 200), (812, 200), (912, 200),
		  (112, 300), (212, 300), (312, 300), (412, 300), (512, 300), (612, 300), (712, 300), (812, 300), (912, 300)], 100, 500)]

pickle.dump(lvls, lvl_file)
lvl_file.close()