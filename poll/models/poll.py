from odoo import models, fields


class PollPoll(models.Model):
    _name = 'poll.poll'
    _description = 'Poll'

    name = fields.Char(string='Poll Title', required=True)
    question_ids = fields.One2many('poll.question', 'poll_id', string='Questions')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)



class PollQustion(models.Model):
    _name = 'poll.question'
    _description = 'Poll Question'

    name = fields.Char(string='Question', required=True)
    poll_id = fields.Many2one('poll.poll', string='Poll', ondelete='cascade')
    answer_ids = fields.One2many('poll.answer', 'question_id', string='Answers')

    # def get_answers(self):
    #     return self.answer_ids
    

class PollAnswer(models.Model):
    _name = 'poll.answer'
    _description = 'Poll Answer'

    name = fields.Char(string='Answer', required=True)
    count = fields.Integer(string='Count', default=0)
    question_id = fields.Many2one('poll.question', string='Question', ondelete='cascade')
    votes = fields.Integer(string='Votes', default=0)

    # def vote(self):
    #     self.votes += 1