import unittest

import tests.test_cpf
import tests.test_cns
import tests.test_cnpj


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(tests.test_cpf))
    suite.addTests(loader.loadTestsFromModule(tests.test_cns))
    suite.addTests(loader.loadTestsFromModule(tests.test_cnpj))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
