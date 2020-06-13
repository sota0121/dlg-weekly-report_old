"""DREP error object."""


class DrepError(Exception):
  """Parent class for user errors or input errors.
  Exceptions of this type are handled by the command line tool
  and result in clear error messages, as opposed to backtraces.
  """
  pass