#!/usr/bin/python
 
'''
	Configuration file storing the dictionary dicoNGramsToInt.
		Key: N-gram;
		Value: Unique integer.
'''


dicoNGramsToInt = { 
	'(0, 0, 37, 39)' : 0, 
	'(0, 3, 23, 29)' : 1, 
	'(0, 9, 37, 39)' : 2, 
	'(0, 37, 0, 37)' : 3, 
	'(0, 37, 37, 0)' : 4, 
	'(0, 37, 37, 37)' : 5, 
	'(0, 37, 39, 29)' : 6, 
	'(0, 37, 39, 37)' : 7, 
	'(0, 37, 39, 39)' : 8, 
	'(0, 37, 39, 63)' : 9, 
	'(0, 48, 7, 27)' : 10, 
	'(3, 23, 7, 29)' : 11, 
	'(3, 23, 7, 30)' : 12, 
	'(3, 23, 8, 7)' : 13, 
	'(3, 23, 29, 0)' : 14, 
	'(3, 23, 29, 29)' : 15, 
	'(3, 23, 29, 37)' : 16, 
	'(6, 0, 37, 39)' : 17, 
	'(6, 3, 23, 7)' : 18, 
	'(6, 3, 23, 29)' : 19, 
	'(6, 6, 29, 29)' : 20, 
	'(6, 9, 3, 23)' : 21, 
	'(6, 9, 39, 63)' : 22, 
	'(6, 9, 63, 62)' : 23, 
	'(6, 29, 6, 3)' : 24, 
	'(6, 29, 6, 29)' : 25, 
	'(6, 29, 6, 37)' : 26, 
	'(6, 29, 9, 6)' : 27, 
	'(6, 29, 9, 37)' : 28, 
	'(6, 29, 29, 29)' : 29, 
	'(6, 29, 29, 37)' : 30, 
	'(6, 29, 29, 39)' : 31, 
	'(6, 29, 29, 63)' : 32, 
	'(6, 29, 37, 6)' : 33, 
	'(6, 29, 37, 29)' : 34, 
	'(6, 29, 37, 37)' : 35, 
	'(6, 29, 37, 39)' : 36, 
	'(6, 29, 37, 60)' : 37, 
	'(6, 29, 37, 63)' : 38, 
	'(6, 29, 61, 29)' : 39, 
	'(6, 37, 6, 3)' : 40, 
	'(6, 37, 6, 29)' : 41, 
	'(6, 37, 6, 37)' : 42, 
	'(6, 37, 6, 42)' : 43, 
	'(6, 37, 6, 63)' : 44, 
	'(6, 37, 9, 23)' : 45, 
	'(6, 37, 37, 0)' : 46, 
	'(6, 37, 37, 29)' : 47, 
	'(6, 37, 37, 37)' : 48, 
	'(6, 38, 29, 29)' : 49, 
	'(6, 39, 3, 23)' : 50, 
	'(6, 39, 9, 3)' : 51, 
	'(6, 39, 29, 9)' : 52, 
	'(6, 39, 29, 29)' : 53, 
	'(6, 39, 29, 37)' : 54, 
	'(6, 39, 37, 37)' : 55, 
	'(6, 42, 9, 3)' : 56, 
	'(6, 42, 9, 37)' : 57, 
	'(6, 42, 29, 9)' : 58, 
	'(6, 42, 63, 62)' : 59, 
	'(6, 63, 62, 29)' : 60, 
	'(7, 10, 59, 7)' : 61, 
	'(7, 10, 59, 18)' : 62, 
	'(7, 26, 18, 45)' : 63, 
	'(7, 27, 29, 29)' : 64, 
	'(7, 27, 29, 37)' : 65, 
	'(7, 28, 0, 3)' : 66, 
	'(7, 28, 9, 63)' : 67, 
	'(7, 28, 29, 0)' : 68, 
	'(7, 28, 29, 29)' : 69, 
	'(7, 29, 7, 10)' : 70, 
	'(7, 29, 9, 37)' : 71, 
	'(7, 29, 37, 63)' : 72, 
	'(7, 30, 7, 29)' : 73, 
	'(7, 30, 7, 30)' : 74, 
	'(7, 30, 18, 7)' : 75, 
	'(7, 30, 29, 9)' : 76, 
	'(7, 30, 29, 37)' : 77, 
	'(7, 64, 29, 48)' : 78, 
	'(8, 7, 29, 7)' : 79, 
	'(8, 7, 30, 18)' : 80, 
	'(9, 0, 9, 37)' : 81, 
	'(9, 0, 37, 39)' : 82, 
	'(9, 3, 23, 7)' : 83, 
	'(9, 3, 23, 8)' : 84, 
	'(9, 3, 23, 29)' : 85, 
	'(9, 6, 9, 3)' : 86, 
	'(9, 6, 9, 63)' : 87, 
	'(9, 6, 29, 6)' : 88, 
	'(9, 6, 29, 9)' : 89, 
	'(9, 6, 29, 37)' : 90, 
	'(9, 6, 37, 6)' : 91, 
	'(9, 6, 39, 3)' : 92, 
	'(9, 6, 39, 9)' : 93, 
	'(9, 6, 39, 29)' : 94, 
	'(9, 6, 42, 9)' : 95, 
	'(9, 9, 3, 23)' : 96, 
	'(9, 9, 9, 23)' : 97, 
	'(9, 9, 23, 8)' : 98, 
	'(9, 9, 23, 45)' : 99, 
	'(9, 23, 7, 29)' : 100, 
	'(9, 23, 8, 7)' : 101, 
	'(9, 23, 29, 29)' : 102, 
	'(9, 23, 29, 37)' : 103, 
	'(9, 29, 29, 39)' : 104, 
	'(9, 29, 37, 29)' : 105, 
	'(9, 29, 37, 39)' : 106, 
	'(9, 29, 37, 60)' : 107, 
	'(9, 29, 39, 29)' : 108, 
	'(9, 29, 60, 29)' : 109, 
	'(9, 37, 0, 9)' : 110, 
	'(9, 37, 6, 29)' : 111, 
	'(9, 37, 29, 37)' : 112, 
	'(9, 37, 37, 0)' : 113, 
	'(9, 37, 37, 6)' : 114, 
	'(9, 37, 37, 37)' : 115, 
	'(9, 37, 39, 6)' : 116, 
	'(9, 37, 39, 29)' : 117, 
	'(9, 37, 60, 6)' : 118, 
	'(9, 39, 63, 62)' : 119, 
	'(9, 60, 37, 6)' : 120, 
	'(9, 63, 62, 29)' : 121, 
	'(10, 59, 7, 64)' : 122, 
	'(10, 59, 18, 7)' : 123, 
	'(18, 7, 26, 18)' : 124, 
	'(18, 7, 29, 7)' : 125, 
	'(18, 7, 30, 18)' : 126, 
	'(23, 7, 29, 9)' : 127, 
	'(23, 7, 29, 37)' : 128, 
	'(23, 7, 30, 7)' : 129, 
	'(23, 7, 30, 29)' : 130, 
	'(23, 7, 30, 45)' : 131, 
	'(23, 8, 7, 29)' : 132, 
	'(23, 8, 7, 30)' : 133, 
	'(23, 29, 0, 48)' : 134, 
	'(23, 29, 29, 29)' : 135, 
	'(23, 29, 29, 37)' : 136, 
	'(23, 29, 29, 39)' : 137, 
	'(23, 29, 29, 57)' : 138, 
	'(23, 29, 29, 63)' : 139, 
	'(23, 29, 37, 3)' : 140, 
	'(23, 29, 37, 6)' : 141, 
	'(23, 29, 37, 29)' : 142, 
	'(23, 29, 37, 37)' : 143, 
	'(23, 29, 37, 63)' : 144, 
	'(27, 29, 29, 9)' : 145, 
	'(27, 29, 29, 29)' : 146, 
	'(27, 29, 29, 37)' : 147, 
	'(27, 29, 29, 63)' : 148, 
	'(27, 29, 37, 3)' : 149, 
	'(27, 29, 37, 37)' : 150, 
	'(27, 29, 37, 63)' : 151, 
	'(28, 0, 3, 23)' : 152, 
	'(28, 9, 63, 62)' : 153, 
	'(28, 29, 0, 3)' : 154, 
	'(28, 29, 29, 0)' : 155, 
	'(28, 29, 29, 29)' : 156, 
	'(29, 0, 3, 23)' : 157, 
	'(29, 0, 37, 39)' : 158, 
	'(29, 0, 48, 7)' : 159, 
	'(29, 6, 3, 23)' : 160, 
	'(29, 6, 9, 3)' : 161, 
	'(29, 6, 29, 6)' : 162, 
	'(29, 6, 29, 29)' : 163, 
	'(29, 6, 29, 37)' : 164, 
	'(29, 6, 37, 9)' : 165, 
	'(29, 6, 37, 37)' : 166, 
	'(29, 6, 63, 62)' : 167, 
	'(29, 7, 10, 59)' : 168, 
	'(29, 9, 3, 23)' : 169, 
	'(29, 9, 6, 29)' : 170, 
	'(29, 9, 6, 37)' : 171, 
	'(29, 9, 9, 23)' : 172, 
	'(29, 9, 23, 7)' : 173, 
	'(29, 9, 23, 8)' : 174, 
	'(29, 9, 29, 39)' : 175, 
	'(29, 9, 37, 6)' : 176, 
	'(29, 9, 37, 60)' : 177, 
	'(29, 9, 60, 37)' : 178, 
	'(29, 9, 63, 62)' : 179, 
	'(29, 29, 0, 3)' : 180, 
	'(29, 29, 0, 37)' : 181, 
	'(29, 29, 6, 3)' : 182, 
	'(29, 29, 6, 9)' : 183, 
	'(29, 29, 6, 29)' : 184, 
	'(29, 29, 6, 63)' : 185, 
	'(29, 29, 9, 9)' : 186, 
	'(29, 29, 9, 23)' : 187, 
	'(29, 29, 29, 0)' : 188, 
	'(29, 29, 29, 6)' : 189, 
	'(29, 29, 29, 29)' : 190, 
	'(29, 29, 29, 37)' : 191, 
	'(29, 29, 29, 39)' : 192, 
	'(29, 29, 29, 42)' : 193, 
	'(29, 29, 29, 48)' : 194, 
	'(29, 29, 29, 63)' : 195, 
	'(29, 29, 37, 6)' : 196, 
	'(29, 29, 37, 29)' : 197, 
	'(29, 29, 37, 37)' : 198, 
	'(29, 29, 37, 39)' : 199, 
	'(29, 29, 37, 60)' : 200, 
	'(29, 29, 37, 63)' : 201, 
	'(29, 29, 39, 3)' : 202, 
	'(29, 29, 39, 6)' : 203, 
	'(29, 29, 39, 9)' : 204, 
	'(29, 29, 39, 29)' : 205, 
	'(29, 29, 39, 37)' : 206, 
	'(29, 29, 39, 63)' : 207, 
	'(29, 29, 42, 48)' : 208, 
	'(29, 29, 42, 63)' : 209, 
	'(29, 29, 48, 7)' : 210, 
	'(29, 29, 57, 29)' : 211, 
	'(29, 29, 63, 62)' : 212, 
	'(29, 37, 3, 23)' : 213, 
	'(29, 37, 6, 3)' : 214, 
	'(29, 37, 6, 29)' : 215, 
	'(29, 37, 29, 6)' : 216, 
	'(29, 37, 29, 37)' : 217, 
	'(29, 37, 29, 39)' : 218, 
	'(29, 37, 37, 0)' : 219, 
	'(29, 37, 37, 6)' : 220, 
	'(29, 37, 37, 29)' : 221, 
	'(29, 37, 37, 37)' : 222, 
	'(29, 37, 37, 42)' : 223, 
	'(29, 37, 39, 37)' : 224, 
	'(29, 37, 60, 9)' : 225, 
	'(29, 37, 63, 62)' : 226, 
	'(29, 39, 3, 23)' : 227, 
	'(29, 39, 6, 9)' : 228, 
	'(29, 39, 6, 29)' : 229, 
	'(29, 39, 6, 37)' : 230, 
	'(29, 39, 9, 23)' : 231, 
	'(29, 39, 9, 29)' : 232, 
	'(29, 39, 29, 6)' : 233, 
	'(29, 39, 29, 9)' : 234, 
	'(29, 39, 29, 29)' : 235, 
	'(29, 39, 29, 39)' : 236, 
	'(29, 39, 37, 6)' : 237, 
	'(29, 39, 37, 9)' : 238, 
	'(29, 39, 37, 29)' : 239, 
	'(29, 39, 37, 37)' : 240, 
	'(29, 39, 63, 62)' : 241, 
	'(29, 42, 48, 7)' : 242, 
	'(29, 42, 63, 62)' : 243, 
	'(29, 48, 7, 27)' : 244, 
	'(29, 48, 7, 28)' : 245, 
	'(29, 57, 29, 37)' : 246, 
	'(29, 57, 37, 37)' : 247, 
	'(29, 60, 29, 37)' : 248, 
	'(29, 61, 29, 29)' : 249, 
	'(29, 61, 29, 37)' : 250, 
	'(29, 63, 62, 7)' : 251, 
	'(29, 63, 62, 29)' : 252, 
	'(29, 63, 62, 37)' : 253, 
	'(30, 7, 29, 37)' : 254, 
	'(30, 7, 30, 7)' : 255, 
	'(30, 7, 30, 29)' : 256, 
	'(30, 7, 30, 45)' : 257, 
	'(30, 18, 7, 29)' : 258, 
	'(30, 18, 7, 30)' : 259, 
	'(30, 29, 9, 37)' : 260, 
	'(30, 29, 9, 60)' : 261, 
	'(30, 29, 37, 63)' : 262, 
	'(37, 0, 0, 37)' : 263, 
	'(37, 0, 9, 37)' : 264, 
	'(37, 0, 37, 0)' : 265, 
	'(37, 0, 37, 37)' : 266, 
	'(37, 0, 37, 39)' : 267, 
	'(37, 3, 23, 29)' : 268, 
	'(37, 6, 3, 23)' : 269, 
	'(37, 6, 6, 29)' : 270, 
	'(37, 6, 29, 6)' : 271, 
	'(37, 6, 29, 9)' : 272, 
	'(37, 6, 29, 29)' : 273, 
	'(37, 6, 29, 37)' : 274, 
	'(37, 6, 29, 61)' : 275, 
	'(37, 6, 37, 6)' : 276, 
	'(37, 6, 42, 29)' : 277, 
	'(37, 6, 63, 62)' : 278, 
	'(37, 9, 3, 23)' : 279, 
	'(37, 9, 6, 9)' : 280, 
	'(37, 9, 6, 29)' : 281, 
	'(37, 9, 6, 39)' : 282, 
	'(37, 9, 6, 42)' : 283, 
	'(37, 9, 9, 3)' : 284, 
	'(37, 9, 9, 9)' : 285, 
	'(37, 9, 23, 29)' : 286, 
	'(37, 9, 29, 37)' : 287, 
	'(37, 9, 63, 62)' : 288, 
	'(37, 29, 6, 3)' : 289, 
	'(37, 29, 6, 63)' : 290, 
	'(37, 29, 9, 6)' : 291, 
	'(37, 29, 29, 37)' : 292, 
	'(37, 29, 29, 39)' : 293, 
	'(37, 29, 37, 37)' : 294, 
	'(37, 29, 37, 60)' : 295, 
	'(37, 29, 37, 63)' : 296, 
	'(37, 29, 39, 37)' : 297, 
	'(37, 37, 0, 0)' : 298, 
	'(37, 37, 0, 37)' : 299, 
	'(37, 37, 6, 6)' : 300, 
	'(37, 37, 6, 29)' : 301, 
	'(37, 37, 6, 37)' : 302, 
	'(37, 37, 6, 63)' : 303, 
	'(37, 37, 9, 9)' : 304, 
	'(37, 37, 29, 9)' : 305, 
	'(37, 37, 29, 29)' : 306, 
	'(37, 37, 29, 37)' : 307, 
	'(37, 37, 37, 0)' : 308, 
	'(37, 37, 37, 29)' : 309, 
	'(37, 37, 37, 37)' : 310, 
	'(37, 37, 37, 42)' : 311, 
	'(37, 37, 42, 63)' : 312, 
	'(37, 39, 3, 23)' : 313, 
	'(37, 39, 6, 9)' : 314, 
	'(37, 39, 6, 29)' : 315, 
	'(37, 39, 6, 37)' : 316, 
	'(37, 39, 6, 39)' : 317, 
	'(37, 39, 6, 42)' : 318, 
	'(37, 39, 9, 3)' : 319, 
	'(37, 39, 29, 9)' : 320, 
	'(37, 39, 29, 37)' : 321, 
	'(37, 39, 29, 57)' : 322, 
	'(37, 39, 37, 9)' : 323, 
	'(37, 39, 37, 37)' : 324, 
	'(37, 39, 37, 39)' : 325, 
	'(37, 39, 39, 3)' : 326, 
	'(37, 39, 39, 6)' : 327, 
	'(37, 39, 39, 9)' : 328, 
	'(37, 39, 39, 29)' : 329, 
	'(37, 39, 39, 37)' : 330, 
	'(37, 39, 39, 39)' : 331, 
	'(37, 39, 63, 62)' : 332, 
	'(37, 42, 63, 62)' : 333, 
	'(37, 60, 6, 29)' : 334, 
	'(37, 60, 6, 38)' : 335, 
	'(37, 60, 9, 0)' : 336, 
	'(37, 60, 9, 29)' : 337, 
	'(37, 60, 9, 37)' : 338, 
	'(37, 63, 62, 7)' : 339, 
	'(37, 63, 62, 29)' : 340, 
	'(38, 29, 29, 29)' : 341, 
	'(39, 3, 23, 29)' : 342, 
	'(39, 6, 0, 37)' : 343, 
	'(39, 6, 9, 3)' : 344, 
	'(39, 6, 9, 39)' : 345, 
	'(39, 6, 9, 63)' : 346, 
	'(39, 6, 29, 6)' : 347, 
	'(39, 6, 29, 37)' : 348, 
	'(39, 6, 29, 61)' : 349, 
	'(39, 6, 37, 6)' : 350, 
	'(39, 6, 37, 37)' : 351, 
	'(39, 6, 39, 3)' : 352, 
	'(39, 6, 39, 9)' : 353, 
	'(39, 6, 39, 29)' : 354, 
	'(39, 6, 39, 37)' : 355, 
	'(39, 6, 42, 9)' : 356, 
	'(39, 6, 42, 63)' : 357, 
	'(39, 9, 3, 23)' : 358, 
	'(39, 9, 23, 29)' : 359, 
	'(39, 9, 29, 29)' : 360, 
	'(39, 29, 6, 37)' : 361, 
	'(39, 29, 9, 3)' : 362, 
	'(39, 29, 9, 23)' : 363, 
	'(39, 29, 9, 29)' : 364, 
	'(39, 29, 9, 37)' : 365, 
	'(39, 29, 9, 63)' : 366, 
	'(39, 29, 29, 6)' : 367, 
	'(39, 29, 29, 29)' : 368, 
	'(39, 29, 29, 39)' : 369, 
	'(39, 29, 37, 29)' : 370, 
	'(39, 29, 37, 39)' : 371, 
	'(39, 29, 37, 60)' : 372, 
	'(39, 29, 39, 29)' : 373, 
	'(39, 29, 57, 37)' : 374, 
	'(39, 37, 6, 29)' : 375, 
	'(39, 37, 9, 3)' : 376, 
	'(39, 37, 9, 6)' : 377, 
	'(39, 37, 9, 9)' : 378, 
	'(39, 37, 9, 29)' : 379, 
	'(39, 37, 9, 63)' : 380, 
	'(39, 37, 29, 29)' : 381, 
	'(39, 37, 37, 0)' : 382, 
	'(39, 37, 37, 6)' : 383, 
	'(39, 37, 37, 9)' : 384, 
	'(39, 37, 37, 29)' : 385, 
	'(39, 37, 37, 37)' : 386, 
	'(39, 37, 39, 3)' : 387, 
	'(39, 37, 39, 6)' : 388, 
	'(39, 37, 39, 9)' : 389, 
	'(39, 37, 39, 37)' : 390, 
	'(39, 39, 3, 23)' : 391, 
	'(39, 39, 6, 0)' : 392, 
	'(39, 39, 6, 9)' : 393, 
	'(39, 39, 6, 29)' : 394, 
	'(39, 39, 6, 37)' : 395, 
	'(39, 39, 6, 39)' : 396, 
	'(39, 39, 6, 42)' : 397, 
	'(39, 39, 9, 3)' : 398, 
	'(39, 39, 29, 37)' : 399, 
	'(39, 39, 37, 37)' : 400, 
	'(39, 39, 39, 37)' : 401, 
	'(39, 63, 62, 29)' : 402, 
	'(42, 9, 3, 23)' : 403, 
	'(42, 9, 37, 37)' : 404, 
	'(42, 29, 9, 3)' : 405, 
	'(42, 48, 7, 28)' : 406, 
	'(42, 63, 62, 29)' : 407, 
	'(42, 63, 62, 37)' : 408, 
	'(48, 7, 27, 29)' : 409, 
	'(48, 7, 28, 0)' : 410, 
	'(48, 7, 28, 9)' : 411, 
	'(48, 7, 28, 29)' : 412, 
	'(57, 29, 37, 39)' : 413, 
	'(57, 37, 37, 0)' : 414, 
	'(57, 37, 37, 37)' : 415, 
	'(59, 7, 64, 29)' : 416, 
	'(59, 18, 7, 26)' : 417, 
	'(60, 6, 29, 29)' : 418, 
	'(60, 6, 38, 29)' : 419, 
	'(60, 9, 0, 9)' : 420, 
	'(60, 9, 0, 37)' : 421, 
	'(60, 9, 29, 37)' : 422, 
	'(60, 9, 29, 60)' : 423, 
	'(60, 9, 37, 0)' : 424, 
	'(60, 9, 37, 29)' : 425, 
	'(60, 9, 37, 37)' : 426, 
	'(60, 29, 37, 60)' : 427, 
	'(60, 37, 6, 29)' : 428, 
	'(61, 29, 29, 29)' : 429, 
	'(61, 29, 37, 29)' : 430, 
	'(61, 29, 37, 63)' : 431, 
	'(62, 7, 30, 7)' : 432, 
	'(62, 7, 30, 29)' : 433, 
	'(62, 29, 29, 9)' : 434, 
	'(62, 29, 29, 29)' : 435, 
	'(62, 29, 29, 37)' : 436, 
	'(62, 29, 29, 39)' : 437, 
	'(62, 29, 29, 63)' : 438, 
	'(62, 29, 37, 3)' : 439, 
	'(62, 29, 37, 6)' : 440, 
	'(62, 29, 37, 29)' : 441, 
	'(62, 29, 37, 37)' : 442, 
	'(62, 29, 37, 63)' : 443, 
	'(62, 29, 48, 7)' : 444, 
	'(62, 37, 29, 37)' : 445, 
	'(62, 37, 37, 37)' : 446, 
	'(63, 62, 7, 30)' : 447, 
	'(63, 62, 29, 29)' : 448, 
	'(63, 62, 29, 37)' : 449, 
	'(63, 62, 29, 48)' : 450, 
	'(63, 62, 37, 29)' : 451, 
	'(63, 62, 37, 37)' : 452, 
	'(64, 29, 48, 7)' : 453, 
}