# coding: utf-8
from datetime import datetime

DB_ENGINE = 'sqlite:///db.sqlite'
AREA_NAME = u'Omaha'
MAP_START = (41.364635, -96.158413)
MAP_END = (41.232025, -95.851332)
GRID = (15, 15)  # row, column
CYCLES_PER_WORKER = 3

SCAN_RADIUS = 70

ACCOUNTS = [
('starrz4', '206739', 'ptc'),
('starrz3', '206739', 'ptc'),
('starrz2', '206739', 'ptc'),
('starrz5', '206739', 'ptc'),
('starrz7', '206739', 'ptc'),
('starrz8', '206739', 'ptc'),
('starrz9', '206739', 'ptc'),
('starrz10', '206739', 'ptc'),
('starrz12', '206739', 'ptc'),
('starrz13', '206739', 'ptc'),
('starrz14', '206739', 'ptc'),
('starrz15', '206739', 'ptc'),
('starrz16', '206739', 'ptc'),
('starrz17', '206739', 'ptc'),
('starrz18', '206739', 'ptc'),
('starrz19', '206739', 'ptc'),
('starrz20', '206739', 'ptc'),
('starrz21', '206739', 'ptc'),
('starrz25', '206739', 'ptc'),
('starrz26', '206739', 'ptc'),
('starrz27', '206739', 'ptc'),
('starrz28', '206739', 'ptc'),
('starrz29', '206739', 'ptc'),
('starrz30', '206739', 'ptc'),
('starrz31', '206739', 'ptc'),
('starrz32', '206739', 'ptc'),
('starrz33', '206739', 'ptc'),
('starrz34', '206739', 'ptc'),
('starrz35', '206739', 'ptc'),
('starrz36', '206739', 'ptc'),
('starrz37', '206739', 'ptc'),
('starrz38', '206739', 'ptc'),
('starrz39', '206739', 'ptc'),
('starrz40', '206739', 'ptc'),
('starrz41', '206739', 'ptc'),
('starrz42', '206739', 'ptc'),
('starrz43', '206739', 'ptc'),
('starrz44', '206739', 'ptc'),
('starrz45', '206739', 'ptc'),
('starrz46', '206739', 'ptc'),
('starrz47', '206739', 'ptc'),
('starrz48', '206739', 'ptc'),
('starrz49', '206739', 'ptc'),
('starrz50', '206739', 'ptc'),
('starrz51', '206739', 'ptc'),
('starrz52', '206739', 'ptc'),
('starrz53', '206739', 'ptc'),
('starrz54', '206739', 'ptc'),
('starrz55', '206739', 'ptc'),
('starrz56', '206739', 'ptc'),
('starrz57', '206739', 'ptc'),
('starrz58', '206739', 'ptc'),
('starrz59', '206739', 'ptc'),
('starrz60', '206739', 'ptc'),
('starrz61', '206739', 'ptc'),
('starrz62', '206739', 'ptc'),
('starrz63', '206739', 'ptc'),
('starrz64', '206739', 'ptc'),
('starrz65', '206739', 'ptc'),
('starrz66', '206739', 'ptc'),
('starrz67', '206739', 'ptc'),
('starrz68', '206739', 'ptc'),
('starrz69', '206739', 'ptc'),
('starrz70', '206739', 'ptc'),
('starrz71', '206739', 'ptc'),
('starrz72', '206739', 'ptc'),
('starrz73', '206739', 'ptc'),
('starrz74', '206739', 'ptc'),
('starrz75', '206739', 'ptc'),
('starrz76', '206739', 'ptc'),
('starrz77', '206739', 'ptc'),
('starrz78', '206739', 'ptc'),
('starrz79', '206739', 'ptc'),
('starrz80', '206739', 'ptc'),
('starrz81', '206739', 'ptc'),
('starrz82', '206739', 'ptc'),
('starrz83', '206739', 'ptc'),
('starrz84', '206739', 'ptc'),
('starrz85', '206739', 'ptc'),
('starrz86', '206739', 'ptc'),
('starrz87', '206739', 'ptc'),
('starrz88', '206739', 'ptc'),
('starrz89', '206739', 'ptc'),
('starrz90', '206739', 'ptc'),
('starrz91', '206739', 'ptc'),
('starrz92', '206739', 'ptc'),
('starrz93', '206739', 'ptc'),
('starrz94', '206739', 'ptc'),
('starrz95', '206739', 'ptc'),
('starrz96', '206739', 'ptc'),
('starrz97', '206739', 'ptc'),
('starrz98', '206739', 'ptc'),
('starrz99', '206739', 'ptc'),
('starrz100', '206739', 'ptc'),
('starrz101', '206739', 'ptc'),
('starrz102', '206739', 'ptc'),
('starrz103', '206739', 'ptc'),
('starrz104', '206739', 'ptc'),
('starrz105', '206739', 'ptc'),
('starrz106', '206739', 'ptc'),
('starrz107', '206739', 'ptc'),
('starrz108', '206739', 'ptc'),
('starrz109', '206739', 'ptc'),
('starrz110', '206739', 'ptc'),
('starrz111', '206739', 'ptc'),
('starrz112', '206739', 'ptc'),
('starrz113', '206739', 'ptc'),
('starrz114', '206739', 'ptc'),
('starrz115', '206739', 'ptc'),
('starrz116', '206739', 'ptc'),
('starrz117', '206739', 'ptc'),
('starrz118', '206739', 'ptc'),
('starrz119', '206739', 'ptc'),
('starrz120', '206739', 'ptc'),
('starrz121', '206739', 'ptc'),
('starrz122', '206739', 'ptc'),
('starrz123', '206739', 'ptc'),
('starrz124', '206739', 'ptc'),
('starrz125', '206739', 'ptc'),
('starrz126', '206739', 'ptc'),
('starrz127', '206739', 'ptc'),
('starrz128', '206739', 'ptc'),
('starrz129', '206739', 'ptc'),
('starrz130', '206739', 'ptc'),
('starrz131', '206739', 'ptc'),
('starrz132', '206739', 'ptc'),
('starrz133', '206739', 'ptc'),
('starrz134', '206739', 'ptc'),
('starrz135', '206739', 'ptc'),
('starrz136', '206739', 'ptc'),
('starrz137', '206739', 'ptc'),
('starrz138', '206739', 'ptc'),
('starrz139', '206739', 'ptc'),
('starrz140', '206739', 'ptc'),
('starrz141', '206739', 'ptc'),
('starrz142', '206739', 'ptc'),
('starrz143', '206739', 'ptc'),
('starrz144', '206739', 'ptc'),
('starrz145', '206739', 'ptc'),
('starrz146', '206739', 'ptc'),
('starrz147', '206739', 'ptc'),
('starrz148', '206739', 'ptc'),
('starrz149', '206739', 'ptc'),
('starrz150', '206739', 'ptc'),
('starrz151', '206739', 'ptc'),
('starrz152', '206739', 'ptc'),
('starrz153', '206739', 'ptc'),
('starrz154', '206739', 'ptc'),
('starrz155', '206739', 'ptc'),
('starrz156', '206739', 'ptc'),
('starrz157', '206739', 'ptc'),
('starrz158', '206739', 'ptc'),
('starrz159', '206739', 'ptc'),
('starrz160', '206739', 'ptc'),
('starrz161', '206739', 'ptc'),
('starrz162', '206739', 'ptc'),
('starrz163', '206739', 'ptc'),
('starrz164', '206739', 'ptc'),
('starrz165', '206739', 'ptc'),
('starrz166', '206739', 'ptc'),
('starrz167', '206739', 'ptc'),
('starrz168', '206739', 'ptc'),
('starrz169', '206739', 'ptc'),
('starrz170', '206739', 'ptc'),
('starrz171', '206739', 'ptc'),
('starrz172', '206739', 'ptc'),
('starrz173', '206739', 'ptc'),
('starrz174', '206739', 'ptc'),
('starrz175', '206739', 'ptc'),
('starrz176', '206739', 'ptc'),
('starrz177', '206739', 'ptc'),
('starrz178', '206739', 'ptc'),
('starrz179', '206739', 'ptc'),
('starrz180', '206739', 'ptc'),
('starrz181', '206739', 'ptc'),
('starrz182', '206739', 'ptc'),
('starrz183', '206739', 'ptc'),
('starrz184', '206739', 'ptc'),
('starrz185', '206739', 'ptc'),
('starrz186', '206739', 'ptc'),
('starrz187', '206739', 'ptc'),
('starrz188', '206739', 'ptc'),
('starrz189', '206739', 'ptc'),
('starrz190', '206739', 'ptc'),
('starrz191', '206739', 'ptc'),
('starrz192', '206739', 'ptc'),
('starrz193', '206739', 'ptc'),
('starrz194', '206739', 'ptc'),
('starrz195', '206739', 'ptc'),
('starrz196', '206739', 'ptc'),
('starrz197', '206739', 'ptc'),
('starrz198', '206739', 'ptc'),
('starrz199', '206739', 'ptc'),
('starrz200', '206739', 'ptc'),
('starrz201', '206739', 'ptc'),
('starrz202', '206739', 'ptc'),
('starrz203', '206739', 'ptc'),
('starrz204', '206739', 'ptc'),
('starrz205', '206739', 'ptc'),
('starrz206', '206739', 'ptc'),
('starrz207', '206739', 'ptc'),
('starrz208', '206739', 'ptc'),
('starrz209', '206739', 'ptc'),
('starrz210', '206739', 'ptc'),
('starrz211', '206739', 'ptc'),
('starrz212', '206739', 'ptc'),
('starrz213', '206739', 'ptc'),
('starrz214', '206739', 'ptc'),
('starrz215', '206739', 'ptc'),
('starrz216', '206739', 'ptc'),
('starrz217', '206739', 'ptc'),
('starrz218', '206739', 'ptc'),
('starrz219', '206739', 'ptc'),
('starrz220', '206739', 'ptc'),
('starrz221', '206739', 'ptc'),
('starrz222', '206739', 'ptc'),
('starrz223', '206739', 'ptc'),
('starrz224', '206739', 'ptc'),
('starrz225', '206739', 'ptc'),
('starrz226', '206739', 'ptc'),
('starrz227', '206739', 'ptc'),
('starrz228', '206739', 'ptc'),
('starrz229', '206739', 'ptc'),
('starrz230', '206739', 'ptc'),
('starrz231', '206739', 'ptc'),

]

TRASH_IDS = [13, 16, 19, 21, 41, 96, 48, 10, 11, 14, 69, 43, 46]
STAGE2 = [94, 139, 141, 149]

REPORT_SINCE = datetime(2016, 7, 29)