# install flask from pip3 with puppet

package {'flask':
  ensur    => 2.1.0,
  provider => pip3
}
