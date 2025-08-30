package org.pcsiszar.corsair.character;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class Attribute {
  String name;
  int value;

  public void increase() {
    value++;
  }
}
