package org.pcsiszar.corsair.character;

import lombok.Data;

@Data
public class AttributePair {
  private Attribute first;
  private Attribute second;

  public Attribute getHigher() {
    return first.getValue() >= second.getValue() ? first : second;
  }

  public Attribute getLower() {
    return first.getValue() <= second.getValue() ? first : second;
  }
}
