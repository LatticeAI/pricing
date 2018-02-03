
mock_train_loss = [
  2.4,
  2.3,
  2.2,
  2.0,
  1.8,
  1.5,
  1.2,
  1.1,
  0.96,
  0.8,
  0.85,
  0.82,
  0.78,
  0.74,
  0.4,
  0.54,
  0.62,
  0.4,
  0.4,
  0.43,
  0.3,
  0.24,
  0.23,
  0.2,
  0.2
]

mock_test_loss = [
  2.4,
  2.2,
  2.1,
  2.1,
  1.9,
  1.8,
  1.7,
  1.4,
  1.3,
  1.05,
  1.0,
  0.95,
  0.8,
  0.8,
  0.7,
  0.5,
  0.5,
  0.5,
  0.5,
  0.53,
  0.49,
  0.30,
  0.32,
  0.30,
  0.31
]


def compute_train_loss(i):
  return mock_train_loss[i]


def compute_test_loss(i):
  return mock_test_loss[i]