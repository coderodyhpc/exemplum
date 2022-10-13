class Dock(QDockWidget):
    def __init__(self, dock_widget: QDockWidget) -> None:   
        super().__init__('GUI')
#_____ TABS SET UP _____#
        tabs = QTabWidget()
        tabs.setStyleSheet('''QTabBar::tab {font-size: 10pt; font-family: Verdana; font-weight: bold; color: #00004F; height: 40px; width: 140px;}''')
        tabs.addTab(WhiteScroll(HomeTab()), 'HOME')
# Properties Tab
        self.genchar_tab = GenCharTab(iface, diebus, self.project)
        tabs.addTab(self.genchar_tab, "SIMULATION\nPROPERTIES")
# General Characteristics Tab
#        self.genchar_tab = GenCharTab(iface, diebus, self.project)
#        tabs.addTab(self.genchar_tab, "GENERAL\nVARIABLES")
# Physics & Dynamics Tab
#        self.physdyn_tab = PhysicsTab(iface, diebus, self.project)
#        tabs.addTab(self.physdyn_tab, "PHYSICS/ \n DYNAMICS")
# Download
        self.download_tab = DownloadTab(iface, diebus, self.project)
        tabs.addTab(self.download_tab, "DOWNLOAD\nMET DATA")
# Preprocessor
        self.preprocessor_tab = PreprocessorTab(iface, diebus, self.project)
#        self.preprocessor_tab = PreprocessorTab(iface)
        tabs.addTab(self.preprocessor_tab, "PREPROCESSOR")
# WRF
        self.WRF_tab = WRFTab(iface, diebus, self.project)
        tabs.addTab(self.WRF_tab, "WRF\nSIMULATIONS")
# S3
        self.S3_tab = S3Tab(iface, diebus)
#        self.S3_tab.setTabDisabled(True)
        tabs.addTab(self.S3_tab, "S3 INTERFACE")
        self.setWidget(tabs)
        self.tabs = tabs
