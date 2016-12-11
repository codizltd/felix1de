# -*- coding: utf-8 -*-
from openerp import fields, models, api
class ProjectIssue(models.Model):
    _inherit='project.issue'
    prm_ticket_id=fields.Char('Ticket-ID')
    #mitarbeiter_id=fields.Many2one('felix1.employees',"Zugewiesener Mitarbeiter")
   # backend_kontakte_id=fields.Many2one('backend.kontakte', string="kontakte")
   # ChamBranch_rel=fields.Many2one('branch.branch', string="Kanzlei-Niederlassung")
   # ToDoPhone=fields.Char( string="Telefon" , related="partner_id.phone")
    rem_Content=fields.Text('Problemloesung')
    frkKathegory_id=fields.Many2one('felix1.ticket.kathegoriess', string='Kathegorie')
    tikDueDate=fields.Date('Faellig Am')
    mandanten_id=fields.Many2one('backend.mandanten', string="Mandanten")
    frkRemark=fields.Text('Bemerkung')
    tikStartDate=fields.Date('Erstellt Am')
    tikCloseDate=fields.Date('Geschlossen Am')
   # ticket_id=fields.Many2one('felix1.ticket', string="Ticket")
class ProjectTask(models.Model):
    _inherit='project.task'
   # product_id=fields.One2many('prject.task.line', 'line')
class BackendLine(models.Model):
    _name='prject.task.line'
    
   # line=fields.Many2one('project.task')
    name=fields.Char('Name')
    monatsgebuhr=fields.Float('Monatsgebuhr')
    einmalgebuhr=fields.Float('Einmalgebuhr')
    jahresgebuhr=fields.Float('Jahresgebuhr')
    #order_id=fields.Many2one('client.order')
