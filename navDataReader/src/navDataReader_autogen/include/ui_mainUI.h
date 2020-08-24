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
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_guiDlg
{
public:
    QVBoxLayout *verticalLayout;
    QVBoxLayout *verticalLayout_2;
    QGridLayout *gridLayout;
    QPushButton *browseButton;
    QSpacerItem *horizontalSpacer;
    QLabel *fName;
    QPushButton *writeButton;
    QSpacerItem *verticalSpacer;
    QHBoxLayout *horizontalLayout_2;
    QSpacerItem *horizontalSpacer_2;
    QLabel *label_2;
    QSpacerItem *horizontalSpacer_3;
    QLabel *plLabel;
    QHBoxLayout *horizontalLayout_3;
    QSpacerItem *horizontalSpacer_4;
    QLabel *label_3;
    QSpacerItem *horizontalSpacer_5;
    QLabel *psLabel;
    QSpacerItem *verticalSpacer_2;
    QTabWidget *tabWidget;
    QWidget *table_view;
    QHBoxLayout *horizontalLayout;
    QTableWidget *tableWidget1;
    QWidget *graph_view;
    QHBoxLayout *horizontalLayout_4;
    QGraphicsView *graphicsView;

    void setupUi(QWidget *guiDlg)
    {
        if (guiDlg->objectName().isEmpty())
            guiDlg->setObjectName(QStringLiteral("guiDlg"));
        guiDlg->resize(849, 506);
        verticalLayout = new QVBoxLayout(guiDlg);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setSizeConstraint(QLayout::SetFixedSize);
        browseButton = new QPushButton(guiDlg);
        browseButton->setObjectName(QStringLiteral("browseButton"));

        gridLayout->addWidget(browseButton, 0, 0, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 2, 1, 1);

        fName = new QLabel(guiDlg);
        fName->setObjectName(QStringLiteral("fName"));

        gridLayout->addWidget(fName, 0, 3, 1, 1);

        writeButton = new QPushButton(guiDlg);
        writeButton->setObjectName(QStringLiteral("writeButton"));
        writeButton->setEnabled(false);

        gridLayout->addWidget(writeButton, 0, 1, 1, 1);


        verticalLayout_2->addLayout(gridLayout);

        verticalSpacer = new QSpacerItem(20, 15, QSizePolicy::Minimum, QSizePolicy::Fixed);

        verticalLayout_2->addItem(verticalSpacer);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalSpacer_2 = new QSpacerItem(100, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_2);

        label_2 = new QLabel(guiDlg);
        label_2->setObjectName(QStringLiteral("label_2"));

        horizontalLayout_2->addWidget(label_2);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_3);

        plLabel = new QLabel(guiDlg);
        plLabel->setObjectName(QStringLiteral("plLabel"));

        horizontalLayout_2->addWidget(plLabel);


        verticalLayout_2->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_4);

        label_3 = new QLabel(guiDlg);
        label_3->setObjectName(QStringLiteral("label_3"));

        horizontalLayout_3->addWidget(label_3);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_5);

        psLabel = new QLabel(guiDlg);
        psLabel->setObjectName(QStringLiteral("psLabel"));

        horizontalLayout_3->addWidget(psLabel);


        verticalLayout_2->addLayout(horizontalLayout_3);

        verticalSpacer_2 = new QSpacerItem(20, 15, QSizePolicy::Minimum, QSizePolicy::Fixed);

        verticalLayout_2->addItem(verticalSpacer_2);

        tabWidget = new QTabWidget(guiDlg);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tabWidget->setTabPosition(QTabWidget::North);
        table_view = new QWidget();
        table_view->setObjectName(QStringLiteral("table_view"));
        horizontalLayout = new QHBoxLayout(table_view);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        tableWidget1 = new QTableWidget(table_view);
        tableWidget1->setObjectName(QStringLiteral("tableWidget1"));
        tableWidget1->horizontalHeader()->setCascadingSectionResizes(true);
        tableWidget1->verticalHeader()->setVisible(false);

        horizontalLayout->addWidget(tableWidget1);

        tabWidget->addTab(table_view, QString());
        graph_view = new QWidget();
        graph_view->setObjectName(QStringLiteral("graph_view"));
        horizontalLayout_4 = new QHBoxLayout(graph_view);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        graphicsView = new QGraphicsView(graph_view);
        graphicsView->setObjectName(QStringLiteral("graphicsView"));

        horizontalLayout_4->addWidget(graphicsView);

        tabWidget->addTab(graph_view, QString());

        verticalLayout_2->addWidget(tabWidget);


        verticalLayout->addLayout(verticalLayout_2);


        retranslateUi(guiDlg);

        tabWidget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(guiDlg);
    } // setupUi

    void retranslateUi(QWidget *guiDlg)
    {
        guiDlg->setWindowTitle(QApplication::translate("guiDlg", "navDataReader", Q_NULLPTR));
        browseButton->setText(QApplication::translate("guiDlg", "Browse File", Q_NULLPTR));
        fName->setText(QApplication::translate("guiDlg", "No file Selected", Q_NULLPTR));
        writeButton->setText(QApplication::translate("guiDlg", "write to CSV", Q_NULLPTR));
        label_2->setText(QApplication::translate("guiDlg", "Path Length", Q_NULLPTR));
        plLabel->setText(QApplication::translate("guiDlg", "None", Q_NULLPTR));
        label_3->setText(QApplication::translate("guiDlg", "Path Smoothness", Q_NULLPTR));
        psLabel->setText(QApplication::translate("guiDlg", "None", Q_NULLPTR));
        tabWidget->setTabText(tabWidget->indexOf(table_view), QApplication::translate("guiDlg", "Table View", Q_NULLPTR));
        tabWidget->setTabText(tabWidget->indexOf(graph_view), QApplication::translate("guiDlg", "Graph View", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class guiDlg: public Ui_guiDlg {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINUI_H
