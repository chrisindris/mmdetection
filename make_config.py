import mmengine

cfg = mmengine.Config.fromfile('./configs/faster_rcnn/faster-rcnn_x101-64x4d_fpn_ms-3x_coco.py')

cfg.data_root = cfg.train_dataloader.dataset.dataset.data_root = cfg.test_dataloader.dataset.data_root = cfg.val_dataloader.dataset.data_root = '/data/Aphid/COCO Format/' #'/content/drive/MyDrive/Aphid Datasets/COCO Format'

cfg.train_dataloader.dataset.dataset.ann_file = '/data/Aphid/COCO Format/annotations/aphid_train_with_iscrowd_segmentation.json'
cfg.test_dataloader.dataset.ann_file = cfg.test_evaluator.ann_file = '/data/Aphid/COCO Format/annotations/aphid_val_with_iscrowd_segmentation.json'
cfg.val_dataloader.dataset.ann_file = cfg.val_evaluator.ann_file = '/data/Aphid/COCO Format/annotations/aphid_val_with_iscrowd_segmentation.json'

cfg.train_dataloader.dataset.dataset.data_prefix = dict(img='train/')
cfg.test_dataloader.dataset.data_prefix = cfg.val_dataloader.dataset.data_prefix = dict(img='val/')

cfg.model.roi_head.bbox_head.num_classes = 1

cfg.train_dataloader.batch_size = cfg.val_dataloader.batch_size = cfg.test_dataloader.batch_size = 7
cfg.train_dataloader.num_workers = cfg.val_dataloader.num_workers = cfg.test_dataloader.num_workers = 4

# for pretraining
#cfg.load_from = '/content/mmdetection/checkpoints/faster_rcnn_x101_64x4d_fpn_mstrain_3x_coco_20210524_124528-26c63de6.pth'
cfg.load_from = '/data/Aphid/epoch_4.pth'

print(cfg.dump())

cfg.dump('./configs/faster_rcnn/faster-rcnn_x101-64x4d_fpn_ms-3x_coco_aphids.py')
