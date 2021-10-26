# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest.mock import patch
from solver import ProblemSolver

# ... définition des fonctions mock_convert et mock_display

class ProblemSolverTest(TestCase):

    def setUp(self):
        with patch('solver.Int2String') as mock:
            mock.convert = mock_convert
            converter = mock
        with patch('solver.Displayer') as mock:
            mock.display = mock_display
            displayer = mock
        self.solver = ProblemSolver(converter, displayer)

# ... méthodes testant le retour d'un appel à self.solver.solve