from collections import deque

def tax_calc(params):
  gross_income = params['gross_income']
  standard_deduction = params['standard_deduction']
  personal_exemption = params['personal_exemption']

  taxable_income = gross_income - standard_deduction - personal_exemption

  brackets = deque(params['brackets'])

  social_security_tax = gross_income * params['social_security_tax_rate']
  medicare_tax        = gross_income * params['medicare_tax_rate']
  income_tax = 0
  while taxable_income > 0:
    current_bracket_taxable_income, rate = brackets.popleft()
    current_bracket_taxable_income = min(taxable_income, current_bracket_taxable_income)
    current_bracket_income_tax = current_bracket_taxable_income * rate

    taxable_income -= current_bracket_taxable_income
    income_tax += current_bracket_income_tax

  total_tax = income_tax + medicare_tax + social_security_tax
  return {
    'income_tax': income_tax,
    'medicare_tax': medicare_tax,
    'social_security': social_security_tax,
    'total_tax': total_tax,
    'effective_income_tax_rate': income_tax/gross_income,
    'effective_total_tax_rate': total_tax/gross_income,
    'take_home': gross_income - total_tax,
  }

def tax_calc_2012(gross_income):
  return tax_calc({
    'gross_income': gross_income,
    'standard_deduction': 5950,
    'personal_exemption': 3800,
    'brackets': [
      (         8700,.10), 
      (        35350,.15),
      (        85650,.25),
      (       178650,.28),
      (       388350,.33),
      ( float("inf"),.35),
    ],
    'social_security_tax_rate': .042,
    'medicare_tax_rate'       : .0145,
  }) 

def main():
  print("What's your gross income?")
  income = int(raw_input())
  tax_info = tax_calc_2012(gross_income=income)
  max_width = max(len(key) for key in tax_info.iterkeys())
  for label, number in tax_info.iteritems():
    print('{0}: {1}'.format(label.rjust(max_width), number))

if __name__ == '__main__':
  main()
