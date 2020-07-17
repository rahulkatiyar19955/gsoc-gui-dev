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
    QTabWidget *tabWidget;
    QWidget *table_view;
    QHBoxLayout *horizontalLayout;
    QTableWidget *tableWidget1;
    QWidget *graph_view;

    void setupUi(QWidget *guiDlg)
    {
        if (guiDlg->objectName().isEmpty())
            guiDlg->setObjectName(QStringLiteral("guiDlg"));
        guiDlg->resize(777, 506);
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

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Fixed);

        verticalLayout_2->addItem(verticalSpacer);

        tabWidget = new QTabWidget(guiDlg);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tabWidget->setTabPosition(QTabWidget::North);
        table_view = new QWidget();
        table_view->setObjectName(QStringLiteral("table_view"));
        horizontalLayout = new QHBoxLayout(table_view);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        tableWidget1 = new QTableWidget(table_view);
        tableWidget1->setObjectName(QStringLiteral("tableWidget1"));

        horizontalLayout->addWidget(tableWidget1);

        tabWidget->addTab(table_view, QString());
        graph_view = new QWidget();
        graph_view->setObjectName(QStringLiteral("graph_view"));
        tabWidget->addTab(graph_view, QString());

        verticalLayout_2->addWidget(tabWidget);


        verticalLayout->addLayout(verticalLayout_2);


        retranslateUi(guiDlg);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(guiDlg);
    } // setupUi

    void retranslateUi(QWidget *guiDlg)
    {
        guiDlg->setWindowTitle(QApplication::translate("guiDlg", "navDataReader", Q_NULLPTR));
        browseButton->setText(QApplication::translate("guiDlg", "Browse Folder", Q_NULLPTR));
        fName->setText(QApplication::translate("guiDlg", "No file Selected", Q_NULLPTR));
        writeButton->setText(QApplication::translate("guiDlg", "write to CSV", Q_NULLPTR));
        tabWidget->setTabText(tabWidget->indexOf(table_view), QApplication::translate("guiDlg", "Table View", Q_NULLPTR));
        tabWidget->setTabText(tabWidget->indexOf(graph_view), QApplication::translate("guiDlg", "Graph View", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class guiDlg: public Ui_guiDlg {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINUI_H
