### Sweet-Chili: Advanced Instance Segmentation for leaf disease detection and Chili stage estimation

Project Context & Problem Statement
Agricultural yield and crop health are threatened by various diseases and growth abnormalities, yet scalable, precise detection solutions remain scarce—especially for specialized crops such as chili peppers. Traditional image datasets and annotation methods often fail to capture the fine-grained, pixel-level details necessary for robust instance segmentation and accurate disease classification. Moreover, the lack of standardized, high-quality datasets for regional plant varieties hinders the deployment of AI-driven solutions in real-world agricultural settings.

##### Chili Disease Detection and Stage Estimation
	• Technical Approach & Solution
		My Solution, Sweet-Chili leverages a custom, research-contributed dataset of chili plant images from Bangladesh, covering a comprehensive range of growth stages (Flower, Green Chili, Red Chili, Rotten Chili, Dry Chili) and disease classes (Bacterial Spot, Curl Virus, Cercospora Leaf Spot, Nutrition Deficiency, White Spot, Healthy Leaves). Images were annotated using high-precision polygonal segmentation and exported in COCO JSON format, enabling pixel-level object localization.
		The solution integrates state-of-the-art deep learning architectures—primarily Mask R-CNN with a ResNet backbone—for instance segmentation and disease detection. Custom PyTorch Dataset loaders parse COCO-style annotations for efficient training and validation. Data augmentation strategies (Albumentations) applied during preprocessing improve model generalization, simulating real-world variations in lighting, orientation, weather, and image quality. The pipeline supports seamless switching between Mask R-CNN and YOLOv8 architectures to benchmark detection and classification performance across models.
		The project employs rigorous evaluation metrics (COCOeval) and modular logging to monitor loss, accuracy, and segmentation quality throughout training. The inclusion of pycocotools, OpenCV, and visual analytics (Matplotlib, Seaborn) ensures transparent evaluation and reproducibility.
##### Goals Achieved & Key Outcomes
			• Developed a domain-specific pipeline for instance segmentation and disease classification of chili plants at the pixel level.
			• Established a high-quality, annotated dataset encompassing critical disease and growth classes, tailored for Southeast Asian agricultural contexts.
			• Achieved robust segmentation and classification accuracy using Mask R-CNN, with dynamic benchmarking against YOLOv8 for object detection.
			• Enabled scalable training and validation with custom PyTorch datasets, advanced augmentation, and COCO-style evaluation.
			• Provided an extensible framework adaptable for other crop types and disease classes.
Impact Sweet-Chili bridges the gap between academic research and practical AI solutions in agriculture, offering a scalable, reproducible pipeline for plant disease detection. By combining localized data, precise annotation, and cutting-edge models, the project empowers agronomists, data scientists, and farmers to improve crop monitoring, disease management, and yield prediction with actionable, AI-driven insights.
