# -*- coding: utf-8 -*-

#SALES.ORDER
from openerp import models, fields, api,_
import methods

class backend_auftraege(models.Model):
    _name='backend.auftraege'
    _inherit='backend.methods.accessid'
    
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Many2one("backend.mandanten", string="Mandant",index=True, ondelete='set null')
    buchungsdatum=fields.Date("Buchungsdatum")
    paket=fields.Many2one("backend.pakete", string="Pakete", index=True, ondelete='set null')
    start=fields.Date("Start")
    ende=fields.Date("Ende")
    umsatz=fields.Monetary("Umsatz")
    bruttoeinnahmen=fields.Monetary("Bruttoeinnahmen")
    arbeitnehmer=fields.Integer("Arbeitnehmer")
    gebuehrmonatsonst=fields.Monetary("GebuehrMonatSonst")
    gebuehrmonatbetriebst=fields.Monetary("GebuehrMonatBetriebSt")
    gebuehrmonatfibu=fields.Monetary("GebuehrMonatFiBu")
    gebuehrmonatfibuueberw=fields.Monetary("GebuehrMonatFiBuUeberw")
    gebuehreinmalsonst=fields.Monetary("GebuehrEinmalSonst")
    gebuehreinmalbetriebst=fields.Monetary("GebuehrEinmalBetriebSt")
    gebuehreinmalfibu=fields.Monetary("GebuehrEinmalFiBu")
    gebuehreinmalfibuueberw=fields.Monetary("GebuehrEinmalFiBuUeberw")
    gebuehrjahrsonst=fields.Monetary("GebuehrJahrSonst")
    gebuehrjahrbetriebst=fields.Monetary("GebuehrJahrBetriebSt")
    gebuehrjahrfibu=fields.Monetary("GebuehrJahrFiBu")
    gebuehrjahrfibuueberw=fields.Monetary("GebuehrJahrFiBuUeberw")
    gebuehrmonat=fields.Monetary("GebuehrMonat")
    gebuehreinmal=fields.Monetary("GebuehrEinmal")
    gebuehrjahr=fields.Monetary("GebuehrJahr")
    bemerkung=fields.Text("Bemerkung")
    start1=fields.Date("Start1")
    ende1=fields.Date("Ende1")
    umsatz1=fields.Monetary("Umsatz1")
    bruttoeinnahmen1=fields.Monetary("Bruttoeinnahmen1")
    arbeitnehmer1=fields.Integer("Arbeitnehmer1")
    gebuehrmonatsonst1=fields.Monetary("GebuehrMonatSonst1")
    gebuehrmonatbetriebst1=fields.Monetary("GebuehrMonatBetriebSt1")
    gebuehrmonatfibu1=fields.Monetary("GebuehrMonatFiBu1")
    gebuehrmonatfibuueberw1=fields.Monetary("GebuehrMonatFiBuUeberw1")
    gebuehreinmalsonst1=fields.Monetary("GebuehrEinmalSonst1")
    gebuehreinmalbetriebst1=fields.Monetary("GebuehrEinmalBetriebSt1")
    gebuehreinmalfibu1=fields.Monetary("GebuehrEinmalFiBu1")
    gebuehreinmalfibuueberw1=fields.Monetary("GebuehrEinmalFiBuUeberw1")
    gebuehrjahrsonst1=fields.Monetary("GebuehrJahrSonst1")
    gebuehrjahrbetriebst1=fields.Monetary("GebuehrJahrBetriebSt1")
    gebuehrjahrfibu1=fields.Monetary("GebuehrJahrFiBu1")
    gebuehrjahrfibuueberw1=fields.Monetary("GebuehrJahrFiBuUeberw1")
    fibuaufsage=fields.Boolean("FiBuAufSage", default=False)
    fibuaufsage1=fields.Boolean("FiBuAufSage1", dafault=False)
    ersteller=fields.Char("Ersteller")
    angelegtam=fields.Date("AngelegtAm")
    angelegtvon=fields.Char("AngelegtVon")
    auftragswert=fields.Monetary("Auftragswert")
    datenok=fields.Boolean("DatenOK", default=False)
    abgerechnet=fields.Boolean("Abgerechnet", default=False)
    currency_id=fields.Many2one('res.currency', string="Währung")