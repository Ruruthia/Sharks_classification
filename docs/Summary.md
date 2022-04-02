# Summary of experiments

In this file, we summarize results of our experiments.
The goal was to train a CNN model for sharks classification tasks.
We intended to compare performance of pretrained ResNet18 model with vanilla CNN trained from scratch.
## ResNet18

The first of the models that we used was [ResNet18](https://arxiv.org/abs/1512.03385).
We finetuned pretrained version from torchvision module by substituting the last layer of classifier.

### Hyperparameters search

We tuned hyperparameters of training scheduler and optimizer such as learning rate, momentum, step size and gamma.
To do so, we used Ray Tune library.
Search space of hyperparameters was as follows:

| Parameter     | Distribution                    |
|---------------|---------------------------------|
| Learning rate | Uniform (0.0001, 0.01)          |
| Momentum      | Uniform (0.05, 0.5)             |
| Step size     | Choice from [1, 2, 4, 6, 8, 10] |
| Gamma         | Uniform (0.05, 0.5)             |

20 models were trained for up to 20 epochs.
Achieved validation accuracy is visualized below:
![](../data/08_reporting/W&B%20Chart%204_2_2022,%206_59_10%20PM.png)

The best model had following hyperparameters: 

| Parameter     | Value                |
|---------------|----------------------|
| Learning rate | 0.004707244812989473 |
| Momentum      | 0.4146024679993903   |
| Step size     | 8                    |
| Gamma         | 0.1292077408885913   |

### Training progress of the best model

**Train accuracy:**
![](../data/08_reporting/W&B%20Chart%204_2_2022,%207_02_28%20PM.png)

The highest train accuracy, equal to 60.24%, was achieved after 12th epoch.

**Train loss:**
![](../data/08_reporting/W&B%20Chart%204_2_2022,%207_02_19%20PM.png)

**Validation accuracy:**
![](../data/08_reporting/W&B%20Chart%204_2_2022,%207_01_51%20PM.png)

The highest validation accuracy, equal to 70.95%, was achieved after 12th epoch.

**Validation loss:**
![](../data/08_reporting/W&B%20Chart%204_2_2022,%207_02_09%20PM.png)

It is surprising that the accuracy and loss results were better on validation rather than training set.
It may be caused by bigger amount of difficult samples in training set and/or data augmentation.

### Results achieved by the best model on test set

#### Metrics

Accuracy was equal to 70.72%, while loss totaled 0.95.

#### Confusion matrix

 ![](../data/08_reporting/resnet_confusion_matrix.png)

It can be noticed that while the model learned to discern most of the classes pretty well, it had some problems when it comes to bull sharks.
In that class case, the majority of samples were misclassified.

#### Examples of misclassified images

Some examples of misclassified samples are visualized below.
It can be noticed that in majority of them,
the face of the shark was cropped, which may have caused difficulties while predicting their class.

 ![](../data/08_reporting/missclassified.png)
 
## Vanilla CNN

TODO