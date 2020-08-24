/********************************************************************************
** Form generated from reading UI file 'mainUI.ui'
**
** Created by: Qt User Interface Compiler version 5.9.5
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINUI_H
#define UI_MAINUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_guiDlg
{
public:
    QHBoxLayout *horizontalLayout_2;
    QTabWidget *tabWidget;
    QWidget *tab1;
    QHBoxLayout *horizontalLayout_4;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout_3;
    QGroupBox *groupBox;
    QHBoxLayout *horizontalLayout;
    QFormLayout *formLayout;
    QLabel *label;
    QLabel *label_2;
    QSpinBox *x_spinbox;
    QSpinBox *z_spinbox;
    QPushButton *send_button;
    QSpacerItem *horizontalSpacer;
    QGroupBox *groupBox_2;
    QHBoxLayout *horizontalLayout_6;
    QVBoxLayout *verticalLayout_13;
    QCheckBox *robotMov_checkbox;
    QCheckBox *autoMov_checkbox;
    QSpacerItem *horizontalSpacer_2;
    QVBoxLayout *verticalLayout_4;
    QHBoxLayout *horizontalLayout_9;
    QLabel *label_5;
    QSlider *ki_slider;
    QHBoxLayout *horizontalLayout_8;
    QLabel *label_4;
    QSlider *ke_slider;
    QSpacerItem *verticalSpacer;
    QWidget *tab;
    QFormLayout *formLayout_2;
    QVBoxLayout *verticalLayout_2;
    QGroupBox *groupBox_3;
    QGridLayout *gridLayout;
    QLabel *label_3;
    QSpinBox *spinBox;
    QLabel *label_6;
    QSpinBox *spinBox_2;
    QGroupBox *groupBox_4;
    QGridLayout *gridLayout_2;
    QLabel *label_7;
    QSpinBox *spinBox_3;
    QLabel *label_8;
    QSpinBox *spinBox_4;
    QVBoxLayout *verticalLayout_3;
    QGroupBox *groupBox_5;
    QGridLayout *gridLayout_3;
    QSlider *horizontalSlider_3;
    QRadioButton *radioButton;
    QRadioButton *radioButton_2;
    QRadioButton *radioButton_3;
    QSlider *horizontalSlider_2;
    QSlider *horizontalSlider;
    QLCDNumber *lcdNumber;
    QLCDNumber *lcdNumber_2;
    QLCDNumber *lcdNumber_3;
    QGroupBox *groupBox_6;
    QGridLayout *gridLayout_4;
    QVBoxLayout *verticalLayout_5;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QSpacerItem *horizontalSpacer_3;
    QSpinBox *deltaV;
    QLabel *label_9;
    QFrame *line_3;
    QHBoxLayout *horizontalLayout_5;
    QProgressBar *progressBar;
    QPushButton *pushButton_3;
    QFrame *line;

    void setupUi(QWidget *guiDlg)
    {
        if (guiDlg->objectName().isEmpty())
            guiDlg->setObjectName(QStringLiteral("guiDlg"));
        guiDlg->resize(788, 353);
        horizontalLayout_2 = new QHBoxLayout(guiDlg);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        tabWidget = new QTabWidget(guiDlg);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tab1 = new QWidget();
        tab1->setObjectName(QStringLiteral("tab1"));
        horizontalLayout_4 = new QHBoxLayout(tab1);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        groupBox = new QGroupBox(tab1);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setMaximumSize(QSize(200, 16777215));
        horizontalLayout = new QHBoxLayout(groupBox);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        formLayout = new QFormLayout();
        formLayout->setObjectName(QStringLiteral("formLayout"));
        formLayout->setLabelAlignment(Qt::AlignCenter);
        label = new QLabel(groupBox);
        label->setObjectName(QStringLiteral("label"));

        formLayout->setWidget(0, QFormLayout::LabelRole, label);

        label_2 = new QLabel(groupBox);
        label_2->setObjectName(QStringLiteral("label_2"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_2);

        x_spinbox = new QSpinBox(groupBox);
        x_spinbox->setObjectName(QStringLiteral("x_spinbox"));
        x_spinbox->setMaximumSize(QSize(150, 16777215));
        x_spinbox->setMinimum(-10000);
        x_spinbox->setMaximum(10000);

        formLayout->setWidget(0, QFormLayout::FieldRole, x_spinbox);

        z_spinbox = new QSpinBox(groupBox);
        z_spinbox->setObjectName(QStringLiteral("z_spinbox"));
        z_spinbox->setMaximumSize(QSize(150, 16777215));
        z_spinbox->setMinimum(-10000);
        z_spinbox->setMaximum(10000);

        formLayout->setWidget(1, QFormLayout::FieldRole, z_spinbox);

        send_button = new QPushButton(groupBox);
        send_button->setObjectName(QStringLiteral("send_button"));
        send_button->setMaximumSize(QSize(100, 16777215));

        formLayout->setWidget(2, QFormLayout::FieldRole, send_button);


        horizontalLayout->addLayout(formLayout);


        horizontalLayout_3->addWidget(groupBox);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer);

        groupBox_2 = new QGroupBox(tab1);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        horizontalLayout_6 = new QHBoxLayout(groupBox_2);
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        verticalLayout_13 = new QVBoxLayout();
        verticalLayout_13->setObjectName(QStringLiteral("verticalLayout_13"));
        robotMov_checkbox = new QCheckBox(groupBox_2);
        robotMov_checkbox->setObjectName(QStringLiteral("robotMov_checkbox"));
        robotMov_checkbox->setChecked(true);

        verticalLayout_13->addWidget(robotMov_checkbox);

        autoMov_checkbox = new QCheckBox(groupBox_2);
        autoMov_checkbox->setObjectName(QStringLiteral("autoMov_checkbox"));
        autoMov_checkbox->setChecked(false);

        verticalLayout_13->addWidget(autoMov_checkbox);


        horizontalLayout_6->addLayout(verticalLayout_13);

        horizontalSpacer_2 = new QSpacerItem(30, 20, QSizePolicy::Maximum, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_2);

        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setObjectName(QStringLiteral("horizontalLayout_9"));
        label_5 = new QLabel(groupBox_2);
        label_5->setObjectName(QStringLiteral("label_5"));

        horizontalLayout_9->addWidget(label_5);

        ki_slider = new QSlider(groupBox_2);
        ki_slider->setObjectName(QStringLiteral("ki_slider"));
        ki_slider->setMaximum(500);
        ki_slider->setValue(120);
        ki_slider->setOrientation(Qt::Horizontal);

        horizontalLayout_9->addWidget(ki_slider);


        verticalLayout_4->addLayout(horizontalLayout_9);

        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setObjectName(QStringLiteral("horizontalLayout_8"));
        label_4 = new QLabel(groupBox_2);
        label_4->setObjectName(QStringLiteral("label_4"));

        horizontalLayout_8->addWidget(label_4);

        ke_slider = new QSlider(groupBox_2);
        ke_slider->setObjectName(QStringLiteral("ke_slider"));
        ke_slider->setMaximum(500);
        ke_slider->setValue(60);
        ke_slider->setSliderPosition(60);
        ke_slider->setOrientation(Qt::Horizontal);

        horizontalLayout_8->addWidget(ke_slider);


        verticalLayout_4->addLayout(horizontalLayout_8);


        horizontalLayout_6->addLayout(verticalLayout_4);


        horizontalLayout_3->addWidget(groupBox_2);


        verticalLayout->addLayout(horizontalLayout_3);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);


        horizontalLayout_4->addLayout(verticalLayout);

        tabWidget->addTab(tab1, QString());
        tab = new QWidget();
        tab->setObjectName(QStringLiteral("tab"));
        formLayout_2 = new QFormLayout(tab);
        formLayout_2->setObjectName(QStringLiteral("formLayout_2"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setSizeConstraint(QLayout::SetDefaultConstraint);
        groupBox_3 = new QGroupBox(tab);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));
        gridLayout = new QGridLayout(groupBox_3);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        label_3 = new QLabel(groupBox_3);
        label_3->setObjectName(QStringLiteral("label_3"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
        label_3->setSizePolicy(sizePolicy);

        gridLayout->addWidget(label_3, 0, 0, 1, 1);

        spinBox = new QSpinBox(groupBox_3);
        spinBox->setObjectName(QStringLiteral("spinBox"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(spinBox->sizePolicy().hasHeightForWidth());
        spinBox->setSizePolicy(sizePolicy1);
        spinBox->setMinimum(-10000);
        spinBox->setMaximum(10000);
        spinBox->setValue(-4500);

        gridLayout->addWidget(spinBox, 0, 1, 1, 1);

        label_6 = new QLabel(groupBox_3);
        label_6->setObjectName(QStringLiteral("label_6"));
        sizePolicy.setHeightForWidth(label_6->sizePolicy().hasHeightForWidth());
        label_6->setSizePolicy(sizePolicy);

        gridLayout->addWidget(label_6, 1, 0, 1, 1);

        spinBox_2 = new QSpinBox(groupBox_3);
        spinBox_2->setObjectName(QStringLiteral("spinBox_2"));
        spinBox_2->setMinimum(-10000);
        spinBox_2->setMaximum(10000);
        spinBox_2->setValue(-2000);

        gridLayout->addWidget(spinBox_2, 1, 1, 1, 1);


        verticalLayout_2->addWidget(groupBox_3);

        groupBox_4 = new QGroupBox(tab);
        groupBox_4->setObjectName(QStringLiteral("groupBox_4"));
        gridLayout_2 = new QGridLayout(groupBox_4);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        label_7 = new QLabel(groupBox_4);
        label_7->setObjectName(QStringLiteral("label_7"));
        sizePolicy.setHeightForWidth(label_7->sizePolicy().hasHeightForWidth());
        label_7->setSizePolicy(sizePolicy);

        gridLayout_2->addWidget(label_7, 0, 0, 1, 1);

        spinBox_3 = new QSpinBox(groupBox_4);
        spinBox_3->setObjectName(QStringLiteral("spinBox_3"));
        sizePolicy1.setHeightForWidth(spinBox_3->sizePolicy().hasHeightForWidth());
        spinBox_3->setSizePolicy(sizePolicy1);
        spinBox_3->setMinimum(-10000);
        spinBox_3->setMaximum(10000);
        spinBox_3->setValue(-400);

        gridLayout_2->addWidget(spinBox_3, 0, 1, 1, 1);

        label_8 = new QLabel(groupBox_4);
        label_8->setObjectName(QStringLiteral("label_8"));
        sizePolicy.setHeightForWidth(label_8->sizePolicy().hasHeightForWidth());
        label_8->setSizePolicy(sizePolicy);

        gridLayout_2->addWidget(label_8, 1, 0, 1, 1);

        spinBox_4 = new QSpinBox(groupBox_4);
        spinBox_4->setObjectName(QStringLiteral("spinBox_4"));
        spinBox_4->setMinimum(-10000);
        spinBox_4->setMaximum(10000);
        spinBox_4->setValue(-2000);

        gridLayout_2->addWidget(spinBox_4, 1, 1, 1, 1);


        verticalLayout_2->addWidget(groupBox_4);


        formLayout_2->setLayout(0, QFormLayout::LabelRole, verticalLayout_2);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        verticalLayout_3->setSizeConstraint(QLayout::SetMinAndMaxSize);
        groupBox_5 = new QGroupBox(tab);
        groupBox_5->setObjectName(QStringLiteral("groupBox_5"));
        gridLayout_3 = new QGridLayout(groupBox_5);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        horizontalSlider_3 = new QSlider(groupBox_5);
        horizontalSlider_3->setObjectName(QStringLiteral("horizontalSlider_3"));
        horizontalSlider_3->setEnabled(false);
        horizontalSlider_3->setValue(20);
        horizontalSlider_3->setOrientation(Qt::Horizontal);

        gridLayout_3->addWidget(horizontalSlider_3, 2, 1, 1, 1);

        radioButton = new QRadioButton(groupBox_5);
        radioButton->setObjectName(QStringLiteral("radioButton"));
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(radioButton->sizePolicy().hasHeightForWidth());
        radioButton->setSizePolicy(sizePolicy2);

        gridLayout_3->addWidget(radioButton, 0, 0, 1, 1);

        radioButton_2 = new QRadioButton(groupBox_5);
        radioButton_2->setObjectName(QStringLiteral("radioButton_2"));

        gridLayout_3->addWidget(radioButton_2, 1, 0, 1, 1);

        radioButton_3 = new QRadioButton(groupBox_5);
        radioButton_3->setObjectName(QStringLiteral("radioButton_3"));

        gridLayout_3->addWidget(radioButton_3, 2, 0, 1, 1);

        horizontalSlider_2 = new QSlider(groupBox_5);
        horizontalSlider_2->setObjectName(QStringLiteral("horizontalSlider_2"));
        horizontalSlider_2->setEnabled(false);
        horizontalSlider_2->setMaximum(500);
        horizontalSlider_2->setValue(60);
        horizontalSlider_2->setOrientation(Qt::Horizontal);

        gridLayout_3->addWidget(horizontalSlider_2, 1, 1, 1, 1);

        horizontalSlider = new QSlider(groupBox_5);
        horizontalSlider->setObjectName(QStringLiteral("horizontalSlider"));
        horizontalSlider->setEnabled(false);
        horizontalSlider->setMaximum(500);
        horizontalSlider->setValue(120);
        horizontalSlider->setOrientation(Qt::Horizontal);

        gridLayout_3->addWidget(horizontalSlider, 0, 1, 1, 1);

        lcdNumber = new QLCDNumber(groupBox_5);
        lcdNumber->setObjectName(QStringLiteral("lcdNumber"));
        QFont font;
        font.setBold(true);
        font.setWeight(75);
        lcdNumber->setFont(font);
        lcdNumber->setLineWidth(0);
        lcdNumber->setSegmentStyle(QLCDNumber::Flat);
        lcdNumber->setProperty("intValue", QVariant(120));

        gridLayout_3->addWidget(lcdNumber, 0, 3, 1, 1);

        lcdNumber_2 = new QLCDNumber(groupBox_5);
        lcdNumber_2->setObjectName(QStringLiteral("lcdNumber_2"));
        lcdNumber_2->setFrameShape(QFrame::NoFrame);
        lcdNumber_2->setLineWidth(1);
        lcdNumber_2->setSegmentStyle(QLCDNumber::Flat);
        lcdNumber_2->setProperty("intValue", QVariant(60));

        gridLayout_3->addWidget(lcdNumber_2, 1, 3, 1, 1);

        lcdNumber_3 = new QLCDNumber(groupBox_5);
        lcdNumber_3->setObjectName(QStringLiteral("lcdNumber_3"));
        lcdNumber_3->setFrameShape(QFrame::NoFrame);
        lcdNumber_3->setLineWidth(1);
        lcdNumber_3->setSegmentStyle(QLCDNumber::Flat);
        lcdNumber_3->setProperty("intValue", QVariant(20));

        gridLayout_3->addWidget(lcdNumber_3, 2, 3, 1, 1);


        verticalLayout_3->addWidget(groupBox_5);

        groupBox_6 = new QGroupBox(tab);
        groupBox_6->setObjectName(QStringLiteral("groupBox_6"));
        QSizePolicy sizePolicy3(QSizePolicy::MinimumExpanding, QSizePolicy::Preferred);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(groupBox_6->sizePolicy().hasHeightForWidth());
        groupBox_6->setSizePolicy(sizePolicy3);
        gridLayout_4 = new QGridLayout(groupBox_6);
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        verticalLayout_5 = new QVBoxLayout();
        verticalLayout_5->setObjectName(QStringLiteral("verticalLayout_5"));
        verticalLayout_5->setSizeConstraint(QLayout::SetMinAndMaxSize);
        pushButton = new QPushButton(groupBox_6);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        sizePolicy2.setHeightForWidth(pushButton->sizePolicy().hasHeightForWidth());
        pushButton->setSizePolicy(sizePolicy2);

        verticalLayout_5->addWidget(pushButton);

        pushButton_2 = new QPushButton(groupBox_6);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        sizePolicy2.setHeightForWidth(pushButton_2->sizePolicy().hasHeightForWidth());
        pushButton_2->setSizePolicy(sizePolicy2);

        verticalLayout_5->addWidget(pushButton_2);


        gridLayout_4->addLayout(verticalLayout_5, 0, 0, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_4->addItem(horizontalSpacer_3, 0, 1, 1, 1);

        deltaV = new QSpinBox(groupBox_6);
        deltaV->setObjectName(QStringLiteral("deltaV"));
        deltaV->setValue(1);

        gridLayout_4->addWidget(deltaV, 0, 3, 1, 1);

        label_9 = new QLabel(groupBox_6);
        label_9->setObjectName(QStringLiteral("label_9"));

        gridLayout_4->addWidget(label_9, 0, 2, 1, 1);


        verticalLayout_3->addWidget(groupBox_6);


        formLayout_2->setLayout(0, QFormLayout::FieldRole, verticalLayout_3);

        line_3 = new QFrame(tab);
        line_3->setObjectName(QStringLiteral("line_3"));
        QSizePolicy sizePolicy4(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(line_3->sizePolicy().hasHeightForWidth());
        line_3->setSizePolicy(sizePolicy4);
        line_3->setMinimumSize(QSize(0, 0));
        line_3->setFrameShadow(QFrame::Sunken);
        line_3->setLineWidth(1);
        line_3->setMidLineWidth(0);
        line_3->setFrameShape(QFrame::HLine);

        formLayout_2->setWidget(1, QFormLayout::FieldRole, line_3);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        progressBar = new QProgressBar(tab);
        progressBar->setObjectName(QStringLiteral("progressBar"));
        progressBar->setEnabled(false);
        progressBar->setValue(0);
        progressBar->setTextVisible(true);
        progressBar->setTextDirection(QProgressBar::TopToBottom);

        horizontalLayout_5->addWidget(progressBar);


        formLayout_2->setLayout(2, QFormLayout::FieldRole, horizontalLayout_5);

        pushButton_3 = new QPushButton(tab);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setEnabled(false);

        formLayout_2->setWidget(2, QFormLayout::LabelRole, pushButton_3);

        tabWidget->addTab(tab, QString());

        horizontalLayout_2->addWidget(tabWidget);

        line = new QFrame(guiDlg);
        line->setObjectName(QStringLiteral("line"));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        horizontalLayout_2->addWidget(line);


        retranslateUi(guiDlg);
        QObject::connect(radioButton, SIGNAL(clicked(bool)), horizontalSlider, SLOT(setEnabled(bool)));
        QObject::connect(radioButton, SIGNAL(clicked(bool)), horizontalSlider_2, SLOT(setDisabled(bool)));
        QObject::connect(radioButton, SIGNAL(clicked(bool)), horizontalSlider_3, SLOT(setDisabled(bool)));
        QObject::connect(radioButton_2, SIGNAL(clicked(bool)), horizontalSlider, SLOT(setDisabled(bool)));
        QObject::connect(radioButton_2, SIGNAL(clicked(bool)), horizontalSlider_2, SLOT(setEnabled(bool)));
        QObject::connect(radioButton_2, SIGNAL(clicked(bool)), horizontalSlider_3, SLOT(setDisabled(bool)));
        QObject::connect(radioButton_3, SIGNAL(clicked(bool)), horizontalSlider_3, SLOT(setEnabled(bool)));
        QObject::connect(radioButton_3, SIGNAL(clicked(bool)), horizontalSlider, SLOT(setDisabled(bool)));
        QObject::connect(radioButton_3, SIGNAL(clicked(bool)), horizontalSlider_2, SLOT(setDisabled(bool)));
        QObject::connect(horizontalSlider, SIGNAL(valueChanged(int)), lcdNumber, SLOT(display(int)));
        QObject::connect(horizontalSlider_2, SIGNAL(valueChanged(int)), lcdNumber_2, SLOT(display(int)));
        QObject::connect(horizontalSlider_3, SIGNAL(valueChanged(int)), lcdNumber_3, SLOT(display(int)));
        QObject::connect(horizontalSlider, SIGNAL(valueChanged(int)), ki_slider, SLOT(setValue(int)));
        QObject::connect(horizontalSlider_2, SIGNAL(valueChanged(int)), ke_slider, SLOT(setValue(int)));

        tabWidget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(guiDlg);
    } // setupUi

    void retranslateUi(QWidget *guiDlg)
    {
        guiDlg->setWindowTitle(QApplication::translate("guiDlg", "navigationComp", Q_NULLPTR));
        groupBox->setTitle(QApplication::translate("guiDlg", "Send to", Q_NULLPTR));
        label->setText(QApplication::translate("guiDlg", "x       ", Q_NULLPTR));
        label_2->setText(QApplication::translate("guiDlg", " z       ", Q_NULLPTR));
        send_button->setText(QApplication::translate("guiDlg", "send", Q_NULLPTR));
        groupBox_2->setTitle(QApplication::translate("guiDlg", "Robot", Q_NULLPTR));
        robotMov_checkbox->setText(QApplication::translate("guiDlg", "Move Robot", Q_NULLPTR));
        autoMov_checkbox->setText(QApplication::translate("guiDlg", "Auto movement", Q_NULLPTR));
        label_5->setText(QApplication::translate("guiDlg", "Internal forces", Q_NULLPTR));
        label_4->setText(QApplication::translate("guiDlg", "External forces", Q_NULLPTR));
        tabWidget->setTabText(tabWidget->indexOf(tab1), QApplication::translate("guiDlg", "Navigation", Q_NULLPTR));
        groupBox_3->setTitle(QApplication::translate("guiDlg", "Initial Position", Q_NULLPTR));
        label_3->setText(QApplication::translate("guiDlg", "X", Q_NULLPTR));
        label_6->setText(QApplication::translate("guiDlg", "Z", Q_NULLPTR));
        groupBox_4->setTitle(QApplication::translate("guiDlg", "target Position", Q_NULLPTR));
        label_7->setText(QApplication::translate("guiDlg", "X", Q_NULLPTR));
        label_8->setText(QApplication::translate("guiDlg", "Z", Q_NULLPTR));
        groupBox_5->setTitle(QApplication::translate("guiDlg", "Variables", Q_NULLPTR));
#ifndef QT_NO_ACCESSIBILITY
        horizontalSlider_3->setAccessibleName(QApplication::translate("guiDlg", "Robot_Speed", Q_NULLPTR));
#endif // QT_NO_ACCESSIBILITY
#ifndef QT_NO_ACCESSIBILITY
        radioButton->setAccessibleName(QString());
#endif // QT_NO_ACCESSIBILITY
        radioButton->setText(QApplication::translate("guiDlg", "internal_Force", Q_NULLPTR));
        radioButton_2->setText(QApplication::translate("guiDlg", "External_Force", Q_NULLPTR));
        radioButton_3->setText(QApplication::translate("guiDlg", "Robot_Speed", Q_NULLPTR));
#ifndef QT_NO_ACCESSIBILITY
        horizontalSlider_2->setAccessibleName(QApplication::translate("guiDlg", "External_Force", Q_NULLPTR));
#endif // QT_NO_ACCESSIBILITY
#ifndef QT_NO_ACCESSIBILITY
        horizontalSlider->setAccessibleName(QApplication::translate("guiDlg", "internal_Force", Q_NULLPTR));
#endif // QT_NO_ACCESSIBILITY
        groupBox_6->setTitle(QApplication::translate("guiDlg", "GroupBox", Q_NULLPTR));
        pushButton->setText(QApplication::translate("guiDlg", "Set Position", Q_NULLPTR));
        pushButton_2->setText(QApplication::translate("guiDlg", "Restart", Q_NULLPTR));
        label_9->setText(QApplication::translate("guiDlg", "Delta", Q_NULLPTR));
        progressBar->setFormat(QApplication::translate("guiDlg", "Optimising %p%", Q_NULLPTR));
        pushButton_3->setText(QApplication::translate("guiDlg", "Start Optimising", Q_NULLPTR));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("guiDlg", "Optimising", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class guiDlg: public Ui_guiDlg {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINUI_H
