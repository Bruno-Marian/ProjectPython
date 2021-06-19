# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.richtext

###########################################################################
## Class menu
###########################################################################

class menu ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 583,293 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel2, 1, wx.ALL|wx.EXPAND, 1 )


		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MSistem", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 24, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel4 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

		self.bt_cadastro = wx.Button( self.m_panel1, wx.ID_ANY, u"Cadastro de Cliente", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.bt_cadastro, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bt_configdb = wx.Button( self.m_panel1, wx.ID_ANY, u"Configuração do banco", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.bt_configdb, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.bt_rel = wx.Button( self.m_panel1, wx.ID_ANY, u"Relatório", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.bt_rel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel3 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bt_cadastro.Bind( wx.EVT_BUTTON, self.OnBtClickbt_cadastro )
		self.bt_configdb.Bind( wx.EVT_BUTTON, self.OnBtClickbt_configdb )
		self.bt_rel.Bind( wx.EVT_BUTTON, self.OnBtClickbt_rel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnBtClickbt_cadastro( self, event ):
		event.Skip()

	def OnBtClickbt_configdb( self, event ):
		event.Skip()

	def OnBtClickbt_rel( self, event ):
		event.Skip()


###########################################################################
## Class rel_client
###########################################################################

class rel_client ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Relatório de cliente", pos = wx.DefaultPosition, size = wx.Size( 990,537 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.grid_rel = wx.grid.Grid( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_rel.CreateGrid( 5, 12 )
		self.grid_rel.EnableEditing( False )
		self.grid_rel.EnableGridLines( False )
		self.grid_rel.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.grid_rel.EnableDragGridSize( False )
		self.grid_rel.SetMargins( 0, 0 )

		# Columns
		self.grid_rel.AutoSizeColumns()
		self.grid_rel.EnableDragColMove( False )
		self.grid_rel.EnableDragColSize( True )
		self.grid_rel.SetColLabelSize( 30 )
		self.grid_rel.SetColLabelValue( 0, u"ID" )
		self.grid_rel.SetColLabelValue( 1, u"NOME" )
		self.grid_rel.SetColLabelValue( 2, u"CPF" )
		self.grid_rel.SetColLabelValue( 3, u"TELEFONE" )
		self.grid_rel.SetColLabelValue( 4, u"RG" )
		self.grid_rel.SetColLabelValue( 5, u"LOGRADOURO" )
		self.grid_rel.SetColLabelValue( 6, u"BAIRRO" )
		self.grid_rel.SetColLabelValue( 7, u"NUMERO" )
		self.grid_rel.SetColLabelValue( 8, u"LOCALIDADE" )
		self.grid_rel.SetColLabelValue( 9, u"UF" )
		self.grid_rel.SetColLabelValue( 10, u"CEP" )
		self.grid_rel.SetColLabelValue( 11, u"DATA_CRIAÇÃO" )
		self.grid_rel.SetColLabelValue( 12, wx.EmptyString )
		self.grid_rel.SetColLabelValue( 13, u"NOME" )
		self.grid_rel.SetColLabelValue( 14, wx.EmptyString )
		self.grid_rel.SetColLabelValue( 15, wx.EmptyString )
		self.grid_rel.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_rel.AutoSizeRows()
		self.grid_rel.EnableDragRowSize( False )
		self.grid_rel.SetRowLabelSize( 0 )
		self.grid_rel.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_rel.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.grid_rel.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		# Cell Defaults
		self.grid_rel.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer11.Add( self.grid_rel, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel11.SetSizer( bSizer11 )
		self.m_panel11.Layout()
		bSizer11.Fit( self.m_panel11 )
		bSizer10.Add( self.m_panel11, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.HORIZONTAL )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.OnActiveRel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnActiveRel( self, event ):
		event.Skip()


###########################################################################
## Class reg_client
###########################################################################

class reg_client ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cadastro de Clientes", pos = wx.DefaultPosition, size = wx.Size( 549,329 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel9 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer7.Add( self.m_panel9, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )


		bSizer6.Add( gbSizer7, 0, wx.EXPAND, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		gbSizer2.SetEmptyCellSize( wx.Size( 0,0 ) )

		gbSizer2.SetMinSize( wx.Size( 10,0 ) )
		self.m_staticText16 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Nome:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText16.Wrap( -1 )

		gbSizer2.Add( self.m_staticText16, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_nome = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer2.Add( self.ed_nome, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText181 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Código:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )

		gbSizer2.Add( self.m_staticText181, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_codigo = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.ed_codigo.Enable( False )

		gbSizer2.Add( self.ed_codigo, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer6.Add( gbSizer2, 0, wx.EXPAND, 5 )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText17 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"CPF:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText17.Wrap( -1 )

		gbSizer3.Add( self.m_staticText17, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_cpf = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gbSizer3.Add( self.ed_cpf, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"RG:", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_staticText18.Wrap( -1 )

		gbSizer3.Add( self.m_staticText18, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_rg = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gbSizer3.Add( self.ed_rg, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer6.Add( gbSizer3, 0, wx.EXPAND, 5 )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText19 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Telefone:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText19.Wrap( -1 )

		gbSizer4.Add( self.m_staticText19, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_telefone = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gbSizer4.Add( self.ed_telefone, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Cep:", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_staticText20.Wrap( -1 )

		gbSizer4.Add( self.m_staticText20, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_cep = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gbSizer4.Add( self.ed_cep, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer6.Add( gbSizer4, 0, wx.EXPAND, 5 )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText21 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Rua:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText21.Wrap( -1 )

		gbSizer5.Add( self.m_staticText21, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_rua = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer5.Add( self.ed_rua, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Numero:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		gbSizer5.Add( self.m_staticText23, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_numero = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		gbSizer5.Add( self.ed_numero, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer6.Add( gbSizer5, 0, wx.EXPAND, 5 )

		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText22 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Bairro:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText22.Wrap( -1 )

		gbSizer6.Add( self.m_staticText22, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ed_bairro = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gbSizer6.Add( self.ed_bairro, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Cidade:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		gbSizer6.Add( self.m_staticText24, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ed_cidade = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gbSizer6.Add( self.ed_cidade, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"UF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		gbSizer6.Add( self.m_staticText25, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ed_uf = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		gbSizer6.Add( self.ed_uf, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer6.Add( gbSizer6, 0, wx.EXPAND, 5 )

		self.m_panel10 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )

		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.bt_cancel = wx.Button( self.m_panel5, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.bt_cancel, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gbSizer8.Add( ( 40, 0 ), wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.bt_salve = wx.Button( self.m_panel5, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.bt_salve, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gbSizer8.Add( ( 40, 0 ), wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.bt_clima = wx.Button( self.m_panel5, wx.ID_ANY, u"Clima", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.bt_clima, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gbSizer8.Add( ( 40, 0 ), wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.bt_pesquisa = wx.Button( self.m_panel5, wx.ID_ANY, u"Pesquisar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.bt_pesquisa, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer6.Add( gbSizer8, 0, wx.EXPAND, 5 )


		self.m_panel5.SetSizer( bSizer6 )
		self.m_panel5.Layout()
		bSizer6.Fit( self.m_panel5 )
		bSizer5.Add( self.m_panel5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.OnActiveClient )
		self.Bind( wx.EVT_SET_FOCUS, self.onsetFocus )
		self.ed_cep.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusEd_cep )
		self.bt_cancel.Bind( wx.EVT_BUTTON, self.OnBtClickbt_cancelar )
		self.bt_salve.Bind( wx.EVT_BUTTON, self.OnBtClickbt_salvar )
		self.bt_clima.Bind( wx.EVT_BUTTON, self.OnBtClimaClick )
		self.bt_pesquisa.Bind( wx.EVT_BUTTON, self.OnBtPesquisaClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnActiveClient( self, event ):
		event.Skip()

	def onsetFocus( self, event ):
		event.Skip()

	def OnKillFocusEd_cep( self, event ):
		event.Skip()

	def OnBtClickbt_cancelar( self, event ):
		event.Skip()

	def OnBtClickbt_salvar( self, event ):
		event.Skip()

	def OnBtClimaClick( self, event ):
		event.Skip()

	def OnBtPesquisaClick( self, event ):
		event.Skip()


###########################################################################
## Class config_db
###########################################################################

class config_db ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 318,277 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel9 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer7.Add( self.m_panel9, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )


		bSizer61.Add( gbSizer7, 0, wx.EXPAND, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		gbSizer2.SetEmptyCellSize( wx.Size( 0,0 ) )

		gbSizer2.SetMinSize( wx.Size( 10,0 ) )
		self.m_staticText16 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Banco:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText16.Wrap( -1 )

		gbSizer2.Add( self.m_staticText16, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_db_name = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer2.Add( self.ed_db_name, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer61.Add( gbSizer2, 0, wx.EXPAND, 5 )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText17 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Local:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText17.Wrap( -1 )

		gbSizer3.Add( self.m_staticText17, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_host = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer3.Add( self.ed_host, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer61.Add( gbSizer3, 0, wx.EXPAND, 5 )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText19 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Porta:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText19.Wrap( -1 )

		gbSizer4.Add( self.m_staticText19, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_port = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer4.Add( self.ed_port, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer61.Add( gbSizer4, 0, wx.EXPAND, 5 )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText21 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Usuário:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText21.Wrap( -1 )

		gbSizer5.Add( self.m_staticText21, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_user = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer5.Add( self.ed_user, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer61.Add( gbSizer5, 0, wx.EXPAND, 5 )

		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText22 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Senha:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText22.Wrap( -1 )

		gbSizer6.Add( self.m_staticText22, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ed_password = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		gbSizer6.Add( self.ed_password, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer61.Add( gbSizer6, 0, wx.EXPAND, 5 )

		self.m_panel10 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer61.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )

		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.bt_cancel = wx.Button( self.m_panel5, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.bt_cancel, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gbSizer8.Add( ( 112, 0 ), wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.bt_salve = wx.Button( self.m_panel5, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.bt_salve, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer61.Add( gbSizer8, 0, wx.EXPAND, 5 )


		self.m_panel5.SetSizer( bSizer61 )
		self.m_panel5.Layout()
		bSizer61.Fit( self.m_panel5 )
		bSizer6.Add( self.m_panel5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.OnActiveConfgDB )
		self.bt_cancel.Bind( wx.EVT_BUTTON, self.OnBtClickbt_cancelar )
		self.bt_salve.Bind( wx.EVT_BUTTON, self.OnBtClickbt_salvar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnActiveConfgDB( self, event ):
		event.Skip()

	def OnBtClickbt_cancelar( self, event ):
		event.Skip()

	def OnBtClickbt_salvar( self, event ):
		event.Skip()


###########################################################################
## Class seach_client
###########################################################################

class seach_client ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 365,398 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.grid_client = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_client.CreateGrid( 15, 3 )
		self.grid_client.EnableEditing( False )
		self.grid_client.EnableGridLines( True )
		self.grid_client.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.grid_client.EnableDragGridSize( False )
		self.grid_client.SetMargins( 0, 0 )

		# Columns
		self.grid_client.EnableDragColMove( False )
		self.grid_client.EnableDragColSize( True )
		self.grid_client.SetColLabelSize( 30 )
		self.grid_client.SetColLabelValue( 0, u"ID" )
		self.grid_client.SetColLabelValue( 1, u"Nome" )
		self.grid_client.SetColLabelValue( 2, u"CPF" )
		self.grid_client.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_client.EnableDragRowSize( True )
		self.grid_client.SetRowLabelSize( 80 )
		self.grid_client.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.grid_client.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.grid_client, 0, 0, 5 )

		gbSizer15 = wx.GridBagSizer( 0, 0 )
		gbSizer15.SetFlexibleDirection( wx.BOTH )
		gbSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Pesquisa:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gbSizer15.Add( self.m_staticText18, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_comboBox2Choices = [ u"Nome", u"CPF" ]
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		gbSizer15.Add( self.m_comboBox2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ed_pesquisa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.ed_pesquisa, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.bt_Pesquisar = wx.Button( self, wx.ID_ANY, u"Pesquisar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.bt_Pesquisar, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer8.Add( gbSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.grid_client.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnDBClickGrid )
		self.bt_Pesquisar.Bind( wx.EVT_BUTTON, self.OnbtPesquisaClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnDBClickGrid( self, event ):
		event.Skip()

	def OnbtPesquisaClick( self, event ):
		event.Skip()


###########################################################################
## Class climate
###########################################################################

class climate ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.TextCtrlClimate = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.TextCtrlClimate.Enable( False )

		bSizer9.Add( self.TextCtrlClimate, 1, wx.EXPAND |wx.ALL, 5 )

		self.bt_close = wx.Button( self, wx.ID_ANY, u"Sair", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.bt_close, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.OnActivateClimate )
		self.bt_close.Bind( wx.EVT_BUTTON, self.bt_Click_sair )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnActivateClimate( self, event ):
		event.Skip()

	def bt_Click_sair( self, event ):
		event.Skip()


