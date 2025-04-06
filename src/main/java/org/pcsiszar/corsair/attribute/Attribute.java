package org.pcsiszar.corsair.attribute;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.ToString;

@RequiredArgsConstructor
@Getter
@EqualsAndHashCode
@ToString
public class Attribute {
  String name;
  double value;

  public void increase() {
    value += 0.5;
  }
}
